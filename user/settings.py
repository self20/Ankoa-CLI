#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
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


iNFOS:

    folder........: source path (ex: /home/toto/torrents/)
    thumb.........: result path (ex: /home/toto/encodes/)
    tag...........: your team name (ex: KULTURA)
    team..........: MEDIAINFO 'Proudly Present' Tag (ex: TEAM KULTURA)
    announce......: your favorite tracker url announce
    tmdb_api_key..: API Key from https://www.themoviedb.org/documentation/api
    tag_thumb.....: Thumbnails tag (ex: <KULTURA PROUDLY PRESENT>)

"""


def option():

    # User Values
    folder = "XXX001"
    thumb = "XXX002"
    tag = "XXX003"
    team = "TEAM XXX003"
    announce = "XXX004"
    tmdb_api_key = "XXX005"
    tag_thumb = "<XXX003 PROUDLY PRESENTS>"

    return (folder, thumb, tag, team, announce, tmdb_api_key, tag_thumb)
