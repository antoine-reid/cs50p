#!/bin/sh

for tonic in C C# Db D D# Eb E F F# Gb G G# Ab A A# Bb B
do
    for type in major minor harmonic melodic
    do
        ./project.py -s ${tonic} -t ${type}
        if [ $? -ne 0 ]; then
            echo "ERROR"
            exit 1
        fi

        ./project.py -s ${tonic} -t ${type} -d
        if [ $? -ne 0 ]; then
            echo "ERROR"
            exit 1
        fi

        ./project.py -s ${tonic} -t ${type} -d -v
        if [ $? -ne 0 ]; then
            echo "ERROR"
            exit 1
        fi
    done
done

for chord in C Cm Co C+ B#m B#o C# C#m C#o C#+ Db Dbm Dbo Db+ D Dm Do D+ Ebb C##m C##o D# D#m D#o D#+ Eb Ebm Ebo Eb+ \
             E Em Eo E+ Fb Fb+ E# E#m E#o F Fm Fo F+ F# F#m F#o F#+ Gb Gbm Gbo Gb+ G Gm Go G+ F##m F##o \
             G# G#m G#o G#+ Ab Abm Abo Ab+ A Am Ao A+ G##o Bbb Bbb+ A# A#m A#o A#+ Bb Bbm Bbo Bb+ B Bm Bo B+ Cb Cbm Cb+
do
    ./project.py -c ${chord}
    if [ $? -ne 0 ]; then
        echo "ERROR"
        exit 1
    fi

    ./project.py -c ${chord} -v
    if [ $? -ne 0 ]; then
        echo "ERROR"
        exit 1
    fi
done

exit 0
