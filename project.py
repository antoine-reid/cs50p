#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import re
import sys
from tabulate import tabulate
from typing import List


class Music_Theory:
    """
    This class is used to group together a bunch of (class) methods, used to compute
    various informations related to Music Theory.

    All of the code in the class is currently implemented as class methods, since no state
    needs to be maintained between calls and no object needs to be instantiated from this class.

    The interesting methods are:

        get_scale: Used to compute the notes of the scales in any key.
                   The supported scales are Major, (Natural) Minor, Harmonic Minor and Melodic Minor

        get_diatonic_chords: Used to compute the list of diatonic chords in any of the supported scales.
                             Diatonic chords are chords that use notes exclusively from the scale.

        get_chord_notes: Used to compute the notes that form a specific triad.
                         The supported triads are:  Major, Minor, Diminished and Augmented

    """

    # This dict is used to find alternate names for enharmonic notes. This is used in scales
    # to make sure each note starts with a consecutive letter, with no duplicates.
    # This means in some cases, we need to introduce double-sharps or double-flats.
    ENHARMONIC_NOTES = {
        "C": ["B#", "Dbb"],
        "C#": ["Db", "B##"],
        "Db": ["C#"],
        "C##": ["D"],
        "D": ["C##", "Ebb"],
        "E": ["Fb", "D##"],
        "E#": ["F"],
        "Fb": ["E"],
        "F": ["E#"],
        "F#": ["Gb", "E##"],
        "Gb": ["F#"],
        "F##": ["G"],
        "G": ["F##", "Abb"],
        "G#": ["Ab", "F###"],
        "G##": ["A"],
        "A": ["G##", "Bbb"],
        "B": ["Cb", "A##"],
        "B#": ["C"],
        "Cb": ["B"],
        "Abb": ["G"],
        "Bbb": ["A"],
        "Ebb": ["D"],
    }

    # Notes of the chromatic scales (starting at C), using sharps or flats
    CHROMATIC_SCALE = {
        "sharps": ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
        "flats": ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"],
    }

    # List of major key signatures, grouped by whether they use sharps or flats
    MAJOR_SCALES = {
        # "C" is included here just to have a default value, even if it has no sharps nor flats
        "sharps": ["C", "G", "D", "A", "E", "B", "F#", "C#"],
        "flats": ["F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"],
    }

    # List of minor key signatures, grouped by whether they use sharps or flats.
    # Note: harmonic minor and melodic minor have some exceptions.
    MINOR_SCALES = {
        # "A" is included here just to have a default value, even if it has no sharps not flats
        "sharps": ["A", "E", "B", "F#", "C#", "G#", "D#", "A#"],
        "flats": ["D", "G", "C", "F", "Bb", "Eb", "Ab"],
    }

    # Chord qualities for each degree, by scale type.
    # "M" == major chord, "m" == minor chord, "o" == diminished chord, "+" == augmented chord
    #
    # For each element, the first list contains our internal symbols and the second
    # list contains the human readable version, ready to display
    SCALE_CHORD_QUALITIES = {
        "major": [
            ["M", "m", "m", "M", "M", "m", "o"],
            ["I", "ii", "iii", "IV", "V", "vi", "viio"],
        ],
        "natural minor": [
            ["m", "o", "M", "m", "m", "M", "M"],
            ["i", "iio", "III", "iv", "v", "VI", "VII"],
        ],
        "harmonic minor": [
            ["m", "o", "+", "m", "M", "M", "o"],
            ["i", "iio", "III+", "iv", "V", "VI", "viio"],
        ],
        "melodic minor": [
            ["m", "m", "+", "M", "M", "o", "o"],
            ["i", "ii", "III+", "IV", "V", "vio", "viio"],
        ],
    }

    # The list of supported scales
    SUPPORTED_SCALES = [
        "major",
        "minor",  # Same as natural minor
        "natural minor",
        "harmonic minor",
        "melodic minor",
    ]

    # Intervals for all the supported scales, in number of half steps (1 == half-step, 2 == whole step)
    # Harmonic minor has a 3 half-steps interval, this is not a typo. Melodic minor should in theory
    # use different intervals when going down the scale, this has not been implemented.
    INTERVALS = {
        "major": [2, 2, 1, 2, 2, 2, 1],
        "natural minor": [2, 1, 2, 2, 1, 2, 2],
        "harmonic minor": [2, 1, 2, 2, 1, 3, 1],
        "melodic minor": [2, 1, 2, 2, 2, 2, 1],
    }

    @classmethod
    def get_enharmonic_note(cls, note: str, expected_note: str | None) -> str:
        if note in cls.ENHARMONIC_NOTES:
            if expected_note:
                for n in cls.ENHARMONIC_NOTES[note]:
                    if n[0] == expected_note:
                        return n
            else:
                return cls.ENHARMONIC_NOTES[note][0]

        if expected_note:
            raise ValueError(
                f"Unable to find enharmonic equivalent for {note} (trying to find {expected_note}"
            )
        else:
            raise ValueError(f"Unable to find enharmonic equivalent for {note}")

    @classmethod
    def get_next_expected_note(cls, note: str) -> str:
        # Find the next expected note name, looping back to "A" after "G"
        original_note = note

        if not 65 <= ord(original_note[0].upper()) <= 71:
            raise ValueError("Invalid note")

        note = chr(ord(original_note[0].upper()) + 1)
        if note == "H":
            note = "A"

        return note

    @classmethod
    def get_intervals(cls, type: str) -> List[int]:
        if type not in cls.SUPPORTED_SCALES:
            raise ValueError("Unsupported scale type")

        if type == "minor":
            # "minor" is an alias for "natural minor"
            type = "natural minor"

        return cls.INTERVALS[type]

    @classmethod
    def get_note_position(cls, note: str, scale: List[str]) -> int:
        for i in range(len(scale)):
            if scale[i] == note:
                return i
        return -1

    @classmethod
    def get_scale(cls, tonic: str, scale: str) -> List[str]:
        if scale not in cls.SUPPORTED_SCALES:
            raise ValueError("Unsupported scale")

        if scale == "minor":
            # "minor" is an alias for "natural minor"
            scale = "natural minor"

        # Pick the correct chromatic scale, with flats or sharps
        # Note: some scales (eg: "D") use sharps in major and flats in minor, so
        # we have to make a distinction here
        if scale == "major":
            if tonic in cls.MAJOR_SCALES["sharps"] or tonic.endswith("#"):
                chromatic_scale = cls.CHROMATIC_SCALE["sharps"]
            else:
                chromatic_scale = cls.CHROMATIC_SCALE["flats"]
        else:
            if tonic in cls.MINOR_SCALES["sharps"] or tonic.endswith("#"):
                chromatic_scale = cls.CHROMATIC_SCALE["sharps"]
            else:
                chromatic_scale = cls.CHROMATIC_SCALE["flats"]

        note_position = cls.get_note_position(tonic, chromatic_scale)
        if note_position == -1:
            # For the tonic, use the first enharmonic note (regular note, not double-flat nor double-sharp)
            # as we are using this to find a starting in the chromatic scale
            temp_tonic = cls.get_enharmonic_note(tonic, None)
            note_position = cls.get_note_position(temp_tonic, chromatic_scale)
            if note_position == -1:
                raise ValueError("Unable to find enharmonic note")

        intervals = cls.get_intervals(scale)

        # The scale always begins with the tonic
        notes = [tonic]

        # Start the loop with previous_note already set to the tonic
        previous_note = tonic

        for interval in intervals:
            # Move forward by the number of specified half-steps
            expected_note_name = cls.get_next_expected_note(previous_note)

            # Calculate what the next note is supposed to be
            note_position = (note_position + interval) % len(chromatic_scale)
            current_note = chromatic_scale[note_position]

            # Since a scale must contain notes with (non-repeating) consecutive note names,
            # find the correct enharmonic if the note name doesn't match what we expect.
            if current_note[0] != expected_note_name:
                current_note = cls.get_enharmonic_note(current_note, expected_note_name)
            notes.append(current_note)
            previous_note = current_note

        return notes

    @classmethod
    def get_diatonic_chords(cls, tonic: str, variant: str) -> List[str]:
        # Diatonic chords are chords that only use the specific notes from a scale.
        # For each degree in a scale, use the quality found in the SCALE_CHORD_QUALITIES
        # dict, based on the scale type. Use the first list, with our internal symbols

        if variant not in cls.SUPPORTED_SCALES:
            raise ValueError("Unsupported scale")

        if variant == "minor":
            # "minor" is an alias for "natural minor"
            variant = "natural minor"

        # Empty list to receive the chords (one per degree) as they get prepared
        chords = []

        # Find all the notes for the requested scale
        notes = cls.get_scale(tonic, variant)

        # For each degree, find the correct chord (with quality) based on the scale type
        for i in range(len(cls.SCALE_CHORD_QUALITIES[variant][0])):
            quality = cls.SCALE_CHORD_QUALITIES[variant][0][i]

            if quality == "M":
                # For Major chords, the "M" should be implicit, so don't include it
                chord = notes[i]
            else:
                # For every other type of chord, append the quality
                chord = notes[i] + quality

            chords.append(chord)

        return chords

    @classmethod
    def get_chord_notes(cls, chord: str) -> List[str]:
        # Get the *major* scale whose tonic is equal to the root note of the requested chord.
        # This will be used to identify the third and fifth notes

        # Get the root note from the chord name (ie: remove any quality)
        root = re.sub(r"(m|o|\+|\-)$", "", chord)
        major_scale = cls.get_scale(root, "major")

        # Empty list to receive the notes as they get prepared
        notes = []

        # All chords start with the root note (inversions are not implemented yet)
        notes.append(root)

        if chord.endswith("m"):
            # Minor chords have a minor third and perfect fifth
            notes.append(cls.flatten(major_scale[2]))
            notes.append(major_scale[4])
        elif chord.endswith("o") or chord.endswith("-"):
            # Diminished chords have a minor third and a diminished fifth
            notes.append(cls.flatten(major_scale[2]))
            notes.append(cls.flatten(major_scale[4]))
        elif chord.endswith("+"):
            # Augmented chords have a major third and augmented fifth
            notes.append(major_scale[2])
            notes.append(cls.sharpen(major_scale[4]))
        else:
            # Any chord without any suffix is implicitly a Major chord.
            # Major chords have a major third and perfect fifth
            notes.append(major_scale[2])
            notes.append(major_scale[4])

        return notes

    @classmethod
    def sharpen(cls, note: str) -> str:
        if note[-1] == "b":
            # To sharpen a note that already has at least one flat symbol, remove one flat
            return note[:-1]
        else:
            # Add one sharp symbol
            # Note: this may result in a note with double-sharp, this is expected in some cases
            return note + "#"

    @classmethod
    def flatten(cls, note: str) -> str:
        if note[-1] == "#":
            # To flatten a note that already has at least one shapr symbol, remove one sharp
            return note[:-1]
        else:
            # Add one flat symbol
            # Note: this may result in a note with double-flat, this is expected in some cases
            return note + "b"


def main():
    ### Parse the command line arguments
    parser = argparse.ArgumentParser(
        description="Compute and display music scales and (optionally) diatonic chords, or the composition of a chord (triad). Please specify either a scale or a single chord."
    )
    parser.add_argument(
        "-s",
        dest="scale",
        help="Display the notes for this SCALE (eg: 'C#'). The type must be provided as well when using this mode",
        required=False,
    )
    parser.add_argument(
        "-t",
        dest="type",
        help="TYPE of scale, select one of the supported scales",
        choices=["major", "minor", "harmonic", "melodic"],
        required=False,
    )
    parser.add_argument(
        "-d",
        dest="diatonic_chords",
        help="Display the DIATONIC chords for the specified scale",
        action="store_true",
        required=False,
    )
    parser.add_argument(
        "-c",
        dest="chord",
        help="Display the notes for a specific CHORD. Add suffix 'm' for minor, 'o' for diminished and '+' for augmented. (Eg: 'C#+' or 'Gbo')",
        required=False,
    )
    parser.add_argument(
        "-v",
        dest="verbose",
        help="VERBOSE mode. Prints '(min)', '(dim)' and '(aug)' next to minor, diminished and augmented degrees and chords",
        action="store_true",
        required=False,
    )
    args = parser.parse_args()

    ### Validate the argument combinations

    # Cannot provide only scale or type. Both must be provided, or none
    if (args.scale and not args.type) or (args.type and not args.scale):
        parser.print_help()
        parser.exit()

    # Cannot request diatonic chords, if no scale has been specified
    if args.diatonic_chords and not (args.scale and args.type):
        parser.print_help()
        parser.exit()

    # Make sure we have at least a scale or a chord
    if not args.scale and not args.chord:
        parser.print_help()
        parser.exit()

    # Requesting scale and chord is not allowed
    if args.scale and args.chord:
        parser.print_help()
        parser.exit()

    if args.scale and args.type:
        # Normalize the scale name and type

        scale_name = args.scale.capitalize()

        scale_types = {
            "major": "major",
            "minor": "natural minor",
            "natural": "natural minor",
            "harmonic": "harmonic minor",
            "melodic": "melodic minor",
        }

        if args.type in scale_types:
            scale_type = scale_types[args.type]

        try:
            notes = get_scale(scale_name, scale_type)
        except ValueError as e:
            print(f"Unable to generate scale: {e}")
            sys.exit(1)

        ## Prepare a table with the notes and print the table

        # The first row is initialized with the proper number of headers, starting at 1
        rows = [range(1, len(notes) + 1)]
        rows.append(notes)

        # Print the table
        print(f"\nNotes for the {scale_name} {scale_type.title()} scale:\n")
        print(
            tabulate(
                rows, headers="firstrow", tablefmt="fancy_outline", stralign="center"
            )
        )
        print()

    if args.diatonic_chords:
        ## Prepare a table with the chords and print the table

        # The first row is initialized with the header names
        rows = [["Degree", "Chord", "Triad"]]

        try:
            chords = get_diatonic_chords(scale_name, scale_type)
            for i in range(len(chords)):
                degree = Music_Theory.SCALE_CHORD_QUALITIES[scale_type][1][i]
                chord_name = chords[i]
                notes = get_chord_notes(chord_name)

                rows.append(
                    [
                        prepare_pretty_display(degree, verbose=args.verbose),
                        prepare_pretty_display(chord_name, verbose=args.verbose),
                        prepare_display_chord_notes(notes),
                    ]
                )
        except ValueError as e:
            print(f"Unable to generate the diatonic chords: {e}")
            sys.exit(2)

        # Print the table
        print(f"\nDiatonic chords for the {scale_name} {scale_type.title()} scale:\n")
        print(
            tabulate(
                rows, headers="firstrow", tablefmt="fancy_outline", stralign="left"
            )
        )
        print()
        sys.exit(0)

    if args.chord:
        try:
            notes = get_chord_notes(args.chord)
        except ValueError as e:
            print(f"Unable to generate the chord: {e}")
            sys.exit(3)

        rows = [["Chord", "Triad"]]
        rows.append(
            [
                prepare_pretty_display(args.chord, verbose=args.verbose),
                prepare_display_chord_notes(notes),
            ]
        )

        # Print the table
        print(
            f"\nNotes in chord {prepare_pretty_display(args.chord, verbose=args.verbose)}:\n"
        )
        print(
            tabulate(
                rows, headers="firstrow", tablefmt="fancy_outline", stralign="left"
            )
        )
        print()

        sys.exit(0)


def get_scale(tonic: str, variant="major") -> List[str]:
    # Use a class method to generate our values
    return Music_Theory.get_scale(tonic, variant)


def get_diatonic_chords(tonic: str, variant="major") -> List[str]:
    # Use a class method to generate our values
    return Music_Theory.get_diatonic_chords(tonic, variant)


def get_chord_notes(chord: str) -> List[str]:
    # Use a class method to generate our values
    return Music_Theory.get_chord_notes(chord)


def prepare_pretty_display(val: str, verbose=False) -> str:
    if val.endswith("o") or val.endswith("-"):
        # Substitute the trailing "o" or "-" (diminished) to a degree sign, to approximate "superscript o"
        val = re.sub(r"[o\-]$", f"\N{DEGREE SIGN}", val)
        if verbose:
            val = val + " (dim)"
    elif val.endswith("+"):
        # Substitute the trailing "+" (augmented) to a superscript +
        val = re.sub(r"\+$", f"\u207A", val)
        if verbose:
            val = val + " (aug)"
    elif val.endswith("m") and verbose:
        val = val + " (min)"

    return val


def prepare_display_chord_notes(notes: List[str], sep=" - ") -> str:
    return sep.join(notes)


if __name__ == "__main__":
    main()
