AnkoA v3.2.5
=====

[**FFMPEG**](https://www.ffmpeg.org/documentation.html) Command Line Easy Encoding Tools ... [**Video Demo**](https://www.youtube.com/watch?v=R_4gfRlgkak&feature=youtu.be)

![AnkoA](http://i.imgur.com/kIZrIVs.png)

## Description :

    Encode or remux your favorites videos simply & quickly
    Bitrate calculator, autocrop, deinterlace, muxing,
    extract subtitles, thumbnails generator, nfo generator,
    prez generator, auto upload thumbnails, auto make .torrent,
    advanced x264/x265 parameters (expert mode), tracks delay (...)

## How to install AnkoA ?

Take a tour on the [**wiki**](https://github.com/AnkoA/AnkoA/wiki)

Chan IRC : **irc.chibi.in/6667 #AnkoA**

## Usage :

* **Easy encoding tool :**
`./ankoa.py`

* **Thumbnails generator :**
`./thumbnails.py source.video 5 2`

* **Upload thumbnails on imgur :**
`./imgur.py thumbnails.png`

* **Genprez :**
`./genprez.py LANGUAGE FORMAT CODECS SUBS SIZE ID_IMDB`

* **NFO generator :**
`./nfogen.sh source.video SOURCE SUBS SUBFORCED URL`

* **Thumbs+nfo+torrent :**
`./make.py source.video SOURCE SUBS SUBFORCED URL`

### Values :

    SOURCE..............: release source     →  1080p.THENiGHTMAREiNHD
    SUBS................: subtitles source   →  FULL.FRENCH.Z1
    SUBFORCED...........: forced subtitles   →  FRENCH.FORCED or N/A
    LANGUAGE............: release language   →  ENGLiSH
    FORMAT..............: release format     →  720p.BluRay
    CODECS..............: release codecs     →  AC3.x264
    SiZE................: release size       →  1.37Go
    iD_iMDB.............: release iMDB iD    →  1121931 (without 'tt')
    URL.................: release infos url  →  http://www.imdb.com/title/tt0315733

#### Command line help :
`(-h or --help)`

![](http://i.imgur.com/QVURs1G.png)

## Version :

Take a tour on the [**changelog**](https://github.com/AnkoA/AnkoA/wiki/changelog)

Author : [**grm34**](https://github.com/grm34)

#### Thanks for assistance and contributions :

* [@thibs](https://github.com/thibs7777777)
* [@Rockweb](https://github.com/Rockweb)
* [@c0ding](https://github.com/c0ding)
* [@Hydrog3n](https://github.com/Hydrog3n)
* [@speedy76](https://github.com/speedy76)

#### Links :

* [AnkoA wiki](https://github.com/AnkoA/AnkoA/wiki)
* [Install or update AnkoA](https://github.com/AnkoA/AnkoA/wiki/Install-or-update-AnkoA)
* [Compile Multimedia Environment](https://github.com/AnkoA/AnkoA/wiki/Compile-Multimedia-Environment)
* [AnkoA global usage](https://github.com/AnkoA/AnkoA/wiki/AnkoA-global-usage)
* [How to crop with AnkoA](https://github.com/AnkoA/AnkoA/wiki/How-to-crop-with-AnkoA)
* [How to use subtitles with AnkoA](https://github.com/AnkoA/AnkoA/wiki/How-to-use-subtitles-with-AnkoA)
* [AnkoA changelog](https://github.com/AnkoA/AnkoA/wiki/Changelog)
* [Video demonstration](https://www.youtube.com/watch?v=R_4gfRlgkak&feature=youtu.be)
* [NFO example](https://github.com/AnkoA/AnkoA/wiki/NFO-Example)

***
### License :

    [AnKoA] Made with love by grm34 (FRIPOUILLEJACK)

    Copyright PARDO Jérémy (Sept 2014)
    Contact: jerem.pardo@gmail.com

    This software is a computer program whose purpose is to help command
    line encoders. Intuitive command line interface with many tools:

    * FFMPEG easy encoding
    * Thumbnails Generator
    * NFO Generator
    * Genprez Upload
    * Auto make .torrent

    This software is governed by the CeCILL-C license under French law and
    abiding by the rules of distribution of free software.  You can  use,
    modify and/or redistribute the software under the terms of the CeCILL-C
    license as circulated by CEA, CNRS and INRIA at the following URL
    "http://www.cecill.info".

    As a counterpart to the access to the source code and  rights to copy,
    modify and redistribute granted by the license, users are provided only
    with a limited warranty  and the software's author,  the holder of the
    economic rights,  and the successive licensors  have only  limited
    liability.

    In this respect, the user's attention is drawn to the risks associated
    with loading,  using,  modifying and/or developing or reproducing the
    software by the user in light of its specific status of free software,
    that may mean  that it is complicated to manipulate,  and  that  also
    therefore means  that it is reserved for developers  and  experienced
    professionals having in-depth computer knowledge. Users are therefore
    encouraged to load and test the software's suitability as regards their
    requirements in conditions enabling the security of their systems and/or
    data to be ensured and,  more generally, to use and operate it in the
    same conditions as regards security.

    The fact that you are presently reading this means that you have had
    knowledge of the CeCILL-C license and that you accept its terms.

***