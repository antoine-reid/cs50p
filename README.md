# Music Scales and Diatonic Chords Generator
#### Video Demo:  https://youtu.be/hyku7Nj4eZ8
#### Description: Compute and display music scales and (optionally) diatonic chords, or the composition of a chord/triad.


# INTRODUCTION

One of the challenges when learning music is to understand and memorize all of the various scales and chords.

In western music, the chromatic scale is built from twelve (12) notes (C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb and B). These are the notes in one octave and correspond to the white and black keys on a piano.

There is exactly one half-step between each note of the chromatic scale.

Notice how some of the note names (letters) have only a half-step in between them, without any sharp or flat note. Specifically, the two pairs in this situation are E-F and B-C.

Also notice that each note, with a sharp or flat, can be called by two names. Either the previous note name with a sharp sign (#), which raises that note by a half-step, or the *next* note with a flat sign (b), which reduces that note by a half-step. These are called enharmonic equivalents and simply represent two different names for the same note (same pitch).

One example would be how C# and Db represent the same sound, yet are called by two different names. Another example would be G# and Ab. Which name is used will depend on the context, as will be explained in the sections below.

# SCALES

## Major Scales

A typical scale is composed of seven (7) out of the possible twelve (12) notes. As we are skipping some of the notes from the chromatic scale, the interval between the notes will usually be either a half-step or a whole step (two half-steps).

In the major scale, these intervals are as follows:

**Formula for the major scale:** W - W - H - W - W - W - H

Starting with the note C and applying the formula for the major scale gives us the familiar C major scale:

**C Major scale:** C, D, E, F, G, A, B

The last half-step in the intervals show that after the seventh note, we add a half-step to cycle back to the beginning of the scale (one octave higher) and this gets us back to our tonic of C.

In C major, using the formula defined above, we end up with a scale that uses only natural notes, that is notes without any accidentals (sharps or flats). It also happens to use all the white keys on a piano.

Of course, scales does not *have* to begin with the C note. If a piece of music was composed with a major scale that starts with a note *other* than C, then applying the same formula as above, we end up with some sharp or flat notes.

One such example would be the key of D major, which requires two sharp notes, to follow the formula above:

**D Major scale:** D, E, F#, G, A, B, C#

## Minor Scales

Not all scales are Major scales however. A lot of interesting music is written using the Minor scale instead.  The logic is exactly as explained above, but using different intervals between the notes.

### Natural Minor Scale

**Formula for the (natural) minor scale:** W - H - W - W - H - W - W

Here is an example of a (natural) minor scale:

**D Minor scale:** D, E, F, G, A, Bb, C, D

Since we want each consecutive note in the scale to use a different name (letter), we do not use A# for the sixth degree, but Bb instead. These are two names for the same note (enharmonic equivalents) and lets us use consecutive names for each note in the scale.

### Additional Minor Scales

To make things even more interesting, there are other types of minor scales, which impact a different mood on the listener.

Two of those additional minor scales are called **harmonic** minor and **melodic** minor.

### Harmonic Minor Scale

**Formula for the harmonic minor scale:** W - H - W - W - H - (W+H) - H

Note how one of the intervals is actually three half-steps (whole + half). Here is an example of a harmonic minor scale:

**G harmonic minor scale:** G, A, Bb, C, D, Eb, F#, G

Interestingly, we end up with both sharps and flats in the same scale! This is required in order to make each note name (letter) unique and consecutive.

### Melodic Minor Scale

**Formula for the melodic minor scale:** W - H - W - W - W - W - H

Here is an example of a melodic minor scale:

**Cb melodic minor scale:** Cb, Db, Ebb, Fb, Gb, Ab, Bb

Note how scales do not always start with a natural note. In this example, this is the C flat melodic minor scale.

Another special case is shown here. In order to make each note name unique and consecutive, we need to have a double-flat note name.

This is related to the fact that some natural notes only have a half-step interval between them (E-F and B-C) so sometimes we will end up with either double-flats or double-sharps in some of the scales.

### Other scales and modes

In music theory, other scales also exist, such as pentatonic scales. These additional scales are out of scope for this project.

Also, other modes exist for the different scales. Modes are called Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian and Locrian.

These various modes are out of scope for this project. Only the Ionian (major scale) and Aeolian (natural minor scale) modes are in scope for this project and supported by the generator.

## DIATONIC CHORDS (TRIADS)

When playing or composing music in a specific key (that is, starting with a specific scale), there are various chords that can be built using exclusively with the notes from that scale. This is especially common when using triads.

Triads are composed of three notes, as their name implies. They are normally constructed by selecting a starting note, skipping the next note, using the next note, skipping another note and finally using the following note.

### Diatonic Chords in a Major Scale

In the scale of C major, the diatonic chord for the first degree (C), would use the notes C - E - G, skipping the notes D and F.

If the same pattern is applied for each degree of the scale, we end up with a list of chords, beginning with each note of the scale respectively, and using only notes found in the scale.

What is *not* obvious though is that in a Major scale, not all of the diatonic chords will be Major chords (root, major third, perfect fifth). In fact, some of the chords will be Minor (root, minor third and perfect fifth) and one of the chord will be a diminished chord (root, minor third and diminished fifth).

This is usually identified like this, for a Major scale:

**Diatonic chords, Major scale:** I, ii, iii, IV, V, vi, vii°

The degrees are written using roman numerals, so that the same notation can always be used regardless of the key signature.

If the degree is written in uppercase, the diatonic chord for this degree is a Major chord. For degrees written in lowercase, the diatonic chord is a Minor chord. Special cases are indicated, such as the 7th degree here being a diminished chord.

For the key of C Major, here are the diatonic chords:

**Diatonic chords, key of C Major:** C, Dm, Em, F, G, Am, B°

It will be no surprise that a lot of classical music is built with the I - IV - V - I chord progression, whichever key signature is used, since those are all major chords.

Things get a lot more interesting for the three Minor scales discussed above.

### Diatonic Chords in a Natural Minor Scale

In a natural minor scale, we have degrees that look *a lot* like the degrees in a major scale, except the list starts at a different position. For example, the diminished chord is now in the second degree instead of the seventh degree.

**Diatonic chords, Natural minor scale:** i, ii°, III, iv, v, VI, VII

Here is an example:

**Diatonic chords, key of F natural minor:** Fm, G°, Ab, Bbm, Cm, Db, Eb

### Diatonic Chords in an Harmonic Minor scale

Since the harmonic minor scale uses a different interval pattern (formula) compared to the natural minor scale, the notes generated are different as well.

A side-effect of this is that the diatonic chords will also be different, since they still need to use only notes that are part of the scale.

**Diatonic chords, Harmonic minor scale:** i, ii°, III⁺, iv, V, VI, vii°

Notice how we now have two major triads, two diminished chords and an augmented chord (root, major third, augmented fifth).

Here is an example:

**Diatonic chords, key of F harmonic minor:** Fm, G°, Ab⁺, Bbm, C, Db, E°

### Diatonic Chords in a Melodic Minor scale

The melodic minor is yet another variation of the minor scale, slightly different than the harmonic minor scale.

**Diatonic chords, Melodic minor scale:** i, ii, III⁺, IV, V, vi°, vii°

Notice how we again have two major triads, two diminished chords and an augmented chord, but not in the same positions as the harmonic minor scale.

Here is an example:

**Diatonic chords, key of F melodic minor:** Fm, Gm, Ab⁺, Bb, C, D°, E°

### Other chords

In music theory, other chords than triads also exist, such as 7th chords, major 7ths, sus2, sus4 and many others. These additional chords are out of scope for this project.

# CONCLUSION

There is a lot of complexity when dealing with Major, Natural Minor, Harmonic Minor and Melodic Minor scales, in all the possible keys.

In addition to having to find or memorize all the notes that are part of the scale for a specific key, a music player or composer has to also remember all of the diatonic chords that use the notes in the key. Then the person needs to know what notes are used to build each of those chords.

When wanting to transpose music in a different key, it is a lot easier to think about it in degrees rather than simply chord names. By using the formulas for the scales and diatonic chords as indicated above, a musician can quickly and easily transpose to a different key.

However, while learning music, it takes a long time to learn and memorize all the combinations.

**Wouldn't it be nice to be able to use an application to calculate and display the scale notes and diatonic chords for any given key?**

**This is precisely what this generator was built for!**

With this generator, you can calculate and display the notes in any given Major, Natural Minor, Harmonic Minor or Melodic Minor key signature. Optionally, you can request the list of diatonic chords (triads) to be shown, along with the three notes that compose each chord.

Another mode when calling the generator is to provide only a triad name to see the three notes that compose it.

The following sections show how to use the generator with examples of the output generated, then  how the code has been laid out and organized in the projects files and source code files.

One of the key challenges (pun intended) is to ensure the code follows all the special rules as explained above:

- Support all the key signatures, for the four supported scale types
- Support keys with a sharp *or* a flat tonic
- Make sure that all the notes use consecutive names (letters), using enharmonic equivalents where required
  - Use double-sharp and double-flats whenever necessary
- When queried for the notes in a triad, support all triads for the supported types (major, minor, diminished, augmented)
  - Support multiple notations for diminished chords
- Support the verbose mode, where Minor, Diminished and Augmented chords are clearly identified

**I hope this generator can be of some use to other people struggling to learn all these scales and chords.**

***

# How to use the Scales and Diatonic Chords Generator

The generator is implemented as a python script and is entirely driven through command-line arguments.

Here are the supported command-line arguments. This help message is automatically generated by ```argparse.ArgumentParser.print_help()```.

```
usage: project.py [-h] [-s SCALE] [-t {major,minor,harmonic,melodic}] [-d] [-c CHORD] [-v]

Compute and display music scales and (optionally) diatonic chords, or the composition of a chord (triad). Please specify either a scale or a single chord.

options:
  -h, --help            show this help message and exit
  -s SCALE              Display the notes for this SCALE (eg: 'C#'). The type must be provided as well when using this mode
  -t {major,minor,harmonic,melodic}
                        TYPE of scale, select one of the supported scales
  -d                    Display the DIATONIC chords for the specified scale
  -c CHORD              Display the notes for a specific CHORD. Add suffix 'm' for minor, 'o' for diminished and '+' for augmented. (Eg: 'C#+' or 'Gbo')
  -v                    VERBOSE mode. Prints '(min)', '(dim)' and '(aug)' next to minor, diminished and augmented degrees and chords
```

## Displaying a scale

As can be seen in the Usage section above, the generator can be used to generate major, (natural) minor, harmonic minor or melodic minor scales.

Here are a few examples:

### C major scale
```
$ ./project.py -s C -t major

Notes for the C Major scale:

╒═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │
╞═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│  C  │  D  │  E  │  F  │  G  │  A  │  B  │  C  │
╘═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛

```

### F sharp harmonic minor scale
```
$ ./project.py -s F# -t harmonic

Notes for the F# Harmonic Minor scale:

╒═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │
╞═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ F#  │ G#  │  A  │  B  │ C#  │  D  │ E#  │ F#  │
╘═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛

```

## Displaying a scale and related diatonic chords

In addition to displaying the notes of a scale, the generator can also display the diatonic chords for each of the scale degrees. Use the '-d' command-line argument to enable the output of diatonic chords.

Diatonic chords are chords that exclusively use notes that are found in the scale. For a major scale, only some of the diatonic chords will be major chords. Some of the chords will have to be minor chords and for the seventh degree, it has to be a diminished chord.

Note how the diminished and augmented chords are listed with the usual notation: '°' for diminished and '⁺' for augmented chords.

In some cases, in order to keep each note in a scale using consecutive letters, we end up having to use double-sharps or double-flats.

Here are a few examples:

### D sharp major scale, with diatonic chords
```
$ ./project.py -s D# -t major -d

Notes for the D# Major scale:

╒═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │
╞═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ D#  │ E#  │ F## │ G#  │ A#  │ B#  │ C## │ D#  │
╘═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛


Diatonic chords for the D# Major scale:

╒══════════╤═════════╤════════════════╕
│ Degree   │ Chord   │ Triad          │
╞══════════╪═════════╪════════════════╡
│ I        │ D#      │ D# - F## - A#  │
│ ii       │ E#m     │ E# - G# - B#   │
│ iii      │ F##m    │ F## - A# - C## │
│ IV       │ G#      │ G# - B# - D#   │
│ V        │ A#      │ A# - C## - E#  │
│ vi       │ B#m     │ B# - D# - F##  │
│ vii°     │ C##°    │ C## - E# - G#  │
╘══════════╧═════════╧════════════════╛

```

### B flat major scale, with diatonic chords
```
$ ./project.py -s Bb -t major -d

Notes for the Bb Major scale:

╒═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │
╞═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ Bb  │  C  │  D  │ Eb  │  F  │  G  │  A  │ Bb  │
╘═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛


Diatonic chords for the Bb Major scale:

╒══════════╤═════════╤═════════════╕
│ Degree   │ Chord   │ Triad       │
╞══════════╪═════════╪═════════════╡
│ I        │ Bb      │ Bb - D - F  │
│ ii       │ Cm      │ C - Eb - G  │
│ iii      │ Dm      │ D - F - A   │
│ IV       │ Eb      │ Eb - G - Bb │
│ V        │ F       │ F - A - C   │
│ vi       │ Gm      │ G - Bb - D  │
│ vii°     │ A°      │ A - C - Eb  │
╘══════════╧═════════╧═════════════╛

```


For natural minor, harmonic minor and melodic minor, some of the notes are different in the scale (different intervals), so the diatonic chords are also different for each degree.


Here are a few examples:

### C sharp (natural) minor scale, with diatonic chords
```
$ ./project.py -s C# -t minor -d

Notes for the C# Natural Minor scale:

╒═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │
╞═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ C#  │ D#  │  E  │ F#  │ G#  │  A  │  B  │ C#  │
╘═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛


Diatonic chords for the C# Natural Minor scale:

╒══════════╤═════════╤═════════════╕
│ Degree   │ Chord   │ Triad       │
╞══════════╪═════════╪═════════════╡
│ i        │ C#m     │ C# - E - G# │
│ ii°      │ D#°     │ D# - F# - A │
│ III      │ E       │ E - G# - B  │
│ iv       │ F#m     │ F# - A - C# │
│ v        │ G#m     │ G# - B - D# │
│ VI       │ A       │ A - C# - E  │
│ VII      │ B       │ B - D# - F# │
╘══════════╧═════════╧═════════════╛

```

### G sharp harmonic minor scale, with diatonic chords
```
$ ./project.py -s G# -t harmonic -d

Notes for the G# Harmonic Minor scale:

╒═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │
╞═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ G#  │ A#  │  B  │ C#  │ D#  │  E  │ F## │ G#  │
╘═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛


Diatonic chords for the G# Harmonic Minor scale:

╒══════════╤═════════╤═══════════════╕
│ Degree   │ Chord   │ Triad         │
╞══════════╪═════════╪═══════════════╡
│ i        │ G#m     │ G# - B - D#   │
│ ii°      │ A#°     │ A# - C# - E   │
│ III⁺     │ B⁺      │ B - D# - F##  │
│ iv       │ C#m     │ C# - E - G#   │
│ V        │ D#      │ D# - F## - A# │
│ VI       │ E       │ E - G# - B    │
│ vii°     │ F##°    │ F## - A# - C# │
╘══════════╧═════════╧═══════════════╛

```

### G flat melodic minor scale, with diatonic chords
```
$ ./project.py -s Gb -t melodic -d

Notes for the Gb Melodic Minor scale:

╒═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │
╞═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ Gb  │ Ab  │ Bbb │ Cb  │ Db  │ Eb  │  F  │ Gb  │
╘═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛


Diatonic chords for the Gb Melodic Minor scale:

╒══════════╤═════════╤═══════════════╕
│ Degree   │ Chord   │ Triad         │
╞══════════╪═════════╪═══════════════╡
│ i        │ Gbm     │ Gb - Bbb - Db │
│ ii       │ Abm     │ Ab - Cb - Eb  │
│ III⁺     │ Bbb⁺    │ Bbb - Db - F  │
│ IV       │ Cb      │ Cb - Eb - Gb  │
│ V        │ Db      │ Db - F - Ab   │
│ vi°      │ Eb°     │ Eb - Gb - Bbb │
│ vii°     │ F°      │ F - Ab - Cb   │
╘══════════╧═════════╧═══════════════╛

```

## Using verbose mode

When displaying diatonic chords (or individual chords, as seen in the next section), it can be difficult to read the symbols for diminished and augmented chords.

By adding the "-v" flag (verbose), the output will change slightly and add a suffix for minor, diminished and augmented chords.

Here is the last example, but with verbose mode enabled:

### G flat melodic minor scale, with diatonic chords and verbose mode
```
$ ./project.py -s Gb -t melodic -d -v

Notes for the Gb Melodic Minor scale:

╒═════╤═════╤═════╤═════╤═════╤═════╤═════╤═════╕
│  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │
╞═════╪═════╪═════╪═════╪═════╪═════╪═════╪═════╡
│ Gb  │ Ab  │ Bbb │ Cb  │ Db  │ Eb  │  F  │ Gb  │
╘═════╧═════╧═════╧═════╧═════╧═════╧═════╧═════╛


Diatonic chords for the Gb Melodic Minor scale:

╒════════════╤════════════╤═══════════════╕
│ Degree     │ Chord      │ Triad         │
╞════════════╪════════════╪═══════════════╡
│ i          │ Gbm (min)  │ Gb - Bbb - Db │
│ ii         │ Abm (min)  │ Ab - Cb - Eb  │
│ III⁺ (aug) │ Bbb⁺ (aug) │ Bbb - Db - F  │
│ IV         │ Cb         │ Cb - Eb - Gb  │
│ V          │ Db         │ Db - F - Ab   │
│ vi° (dim)  │ Eb° (dim)  │ Eb - Gb - Bbb │
│ vii° (dim) │ F° (dim)   │ F - Ab - Cb   │
╘════════════╧════════════╧═══════════════╛

```

## Displaying the notes of a specific chord (triad)

A simpler mode is also provided with the generator. By using the "-c CHORD" command-line argument, a specific chord name can be specified and the generator will display the notes (triad) for that chord. Only major, minor, diminished and augmented chords are supported at this time.

Use a lowercase "o" suffix for diminished or a "+" suffix for augmented.

The "-v" flag can also be used in conjunction with "-c".

Here are a few examples:

### A flat augmented chord
```
$ ./project.py -c Ab+

Notes in chord Ab⁺:

╒═════════╤════════════╕
│ Chord   │ Triad      │
╞═════════╪════════════╡
│ Ab⁺     │ Ab - C - E │
╘═════════╧════════════╛

```

### A flat augmented chord, with verbose mode
```
$ ./project.py -c Ab+ -v

Notes in chord Ab⁺ (aug):

╒═══════════╤════════════╕
│ Chord     │ Triad      │
╞═══════════╪════════════╡
│ Ab⁺ (aug) │ Ab - C - E │
╘═══════════╧════════════╛

```

### G sharp diminished chord, with verbose mode

This is the first supported syntax to request a diminished chord, using an "o" suffix.

```
$ ./project.py -c G#o -v

Notes in chord G#° (dim):

╒═══════════╤════════════╕
│ Chord     │ Triad      │
╞═══════════╪════════════╡
│ G#° (dim) │ G# - B - D │
╘═══════════╧════════════╛

```

### D flat diminished chord, with verbose mode

This is the other supported syntax to request a diminished chord, using a "-" suffix.

```
./project.py -c Db- -v

Notes in chord Db° (dim):

╒═══════════╤═══════════════╕
│ Chord     │ Triad         │
╞═══════════╪═══════════════╡
│ Db° (dim) │ Db - Fb - Abb │
╘═══════════╧═══════════════╛

```

***

# Project files and source code organization

Here is a list of files included in the project. All the Python files successfully pass the checks executed by ```mypy```.

In addition, the main ```project.py``` file fully complies with the style checked by ```style50```.

The file ```test_project.py``` complies *in spirit* with ```style50``` except for line lengths. It is the author's opinion that the longer lines in the current file are legible enough and do not warrant breaking down the lists on multiple lines, as suggested by ```style50```. Since the scales have a predetermined length, it is unlikely that this test code would be modified to add more elements to those lists. Running "black -l 110 test_project.py" (for longer line lengths) leaves the file unchanged.


## File: README.md

This document.

## File: requirements.txt

This file contains a list of Python packages (installable via ```pip```), which must be present for the code to run.

Here are the required packages:
- tabulate
- types-tabulate
  - used to allow mypy to check the type hints for tabulate

## File: project.py

### Top-level functions

The project code is located in the main project.py file. There is a main() function defined, which first parses the command-line arguments and then calls some top-level functions.

Here are the top-level functions defined:

- ```get_scale()```
  - Wrapper around ```Music_Theory.get_scale()```
- ```get_diatonic_chords()```
  - Wrapper around ```Music_Theory.get_diatonic_chords()```
- ```get_chord_notes()```
  - Wrapper around ```Music_Theory.get_chord_notes()```
- ```prepare_pretty_display()```
  - Adjusts the display of a chord name, replacing a trailing "o" or "+" by "°" and "⁺" respectively. Also adds "(min)", "(dim)" or "(aug)" in verbose mode.
- ```prepare_display_chord_notes()```
  - Prepares the display of a chord triad, using a text separator. The default separator is " - " but it can be specified as an optional parameter.

The last two functions are helper functions that are used to adjust the formatting of some values, for display purposes only. They are used for diminished and augmented chords, or for formatting a chord (triad).

### Class: Music_Theory

Most of the real logic is implemented in the ```Music_Theory``` class though, also located in the ```project.py``` file. This class could be refactored in a separate module or even as a package, to make the code easily reusable.

The class has a few class variables that hold some constant values, such as chromatic scales, lists of scales that use sharps or flats, etc.

Here are the class variables defined:
- ```ENHARMONIC_NOTES```
  - dict of lists. Contains all the enharmonic equivalents for a specific note. eg: "C": ["B#", "Dbb"]
- ```CHROMATIC_SCALE```
  - dict of lists. For sharps and flats, contains a chromatic scale starting with "C"
- ```MAJOR_SCALES```
  - dict of lists. For sharps and flats, contains a list of major scales that use some sharp or flat notes, respectively.
- ```MINOR_SCALES```
  - dict of lists. For sharps and flats, contains a list of minor scales that use mostly sharp or flat notes, respectively.
- ```SCALE_CHORD_QUALITIES```
  - dict of lists of lists. For each scale type, contains a list of two lists, containing chord suffixes and degree qualities, respectively
- ```SUPPORTED_SCALES```
  - list of the scale types supported by this generator
- ```INTERVALS```
  - dict of lists. For each scale type, contains a list of intervals, expressed as a number of half-steps (integers)

Most of those class variables are actually dictionaries, to allow adding more scale types in the future.

```Music_Theory``` currently provides and uses class methods exclusively. There are no properties nor any state to maintain between invocation of any of those methods.
Therefore, there is no need to instantiate an object from the class. All the methods have been decorated with ```@classmethod```.

Here is a list of the class methods:
- ```Music_Theory.get_scale()```
  - Used to generate a list of all the notes for a given key signature
- ```Music_Theory.get_diatonic_chords()```
  - Used to generate a list of all the diatonic chord names for a given key signature
- ```Music_Theory.get_chord_notes()```
  - Used to generate a list of three notes for a given chord name (triad)
- ```Music_Theory.sharpen()```
  - Internal method, used to sharpen a given note
- ```Music_Theory.flatten()```
  - Internal method, used to flatten a given note
- ```Music_Theory.get_enharmonic_note()```
  - Internal method, used to find an enharmonic equivalent, given a starting note and a desired note (letter)
- ```Music_Theory.get_next_expected_note()```
  - Internal method, used to find the next expected note name (letter)
- ```Music_Theory.get_intervals()```
  - Internal method, used to get the intervals for a given scale type. Aliases "minor" to "natural minor"
- ```Music_Theory.get_note_position()```
  - Internal method, used to find the position (index) of a specified note in a given scale, usually in the chromatic scale

All the functions and methods have type hints added, both for the arguments/parameters and the return values.

## File: test_project.py

The ```test_project.py``` file contains all the tests that can be executed by ```pytest```.

These are the functions that test the top-level functions in the ```project.py``` file:
- ```test_get_scale()```
  - tests as many combinations of key signatures as possible (tonics and scale types), to catch any corner case
- ```test_get_diatonic_chords()```
  - tests as many combinations as possible again, to catch any corner case
- ```test_get_chord_notes()```
  - tests all the chords generated by the ```get_diatonic_chords()``` calls in the previous function
- ```test_prepare_pretty_display()```
  - tests the ```prepare_pretty_display()``` function
- ```test_prepare_display_chord_notes()```
  - tests the ```prepare_display_chord_notes()``` function

In addition, there are also additional test functions, defined to directly test the class methods in Music_Theory:
- ```test_get_enharmonic_note()```
  - test ```Music_Theory.get_enharmonic_note()```
- ```test_get_next_expected_note()```
  - test ```Music_Theory.get_next_expected_note(```
- ```test_get_intervals()```
  - test ```Music_Theory.get_intervals()```
- ```test_get_note_position()```
  - test ```Music_Theory.get_note_position()```
- ```test_sharpen()```
  - test ```Music_Theory.sharpen()```
- ```test_flatten()```
  - test ```Music_Theory.flatten()```

## File: run_all.sh

The shell script called ```run_all.sh``` uses shell loops to execute the python script with various combinations of command-line arguments.

In case any of the invocations of the python script exits with a value other than zero (0), the shell script will display an error and stop.
