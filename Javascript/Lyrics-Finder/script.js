var searchTerms; //The value entered into the search box.
var trackID; //The ID created in the getTrack function for use in the returnLyrics function. 
var resultsSection = document.getElementById("results"); //the html div used to display the results of each ajax call
var backButton = document.getElementById("back-button-container"); //container for button for the user to navigate between results pages

//checkRadio is run when the user clicks on the Search button
function checkRadio() {
    searchTerms = document.getElementById("search").value;
    if ($("#artistRadioButton").is(":checked")) {
        getArtist();
    }
    else {
        getTrack();
    }
}

//To reset the page when results are displayed.
function resetPage() {
    resultsSection.innerHTML = "";
    backButton.innerHTML = "";
}

//If 'song' radio button is selected:
function getTrack() {
    resetPage();
    $.ajax({
            type: "GET",
            data: {
                apikey: "e0d06b2c7958ae772bc22de9f61bce97",
                q_track: searchTerms, //queries by song name
                format: "jsonp",
                callback: "jsonp_callback",
                page_size: 100, //returns the first 100 results
                s_artist_rating: "DESC", //sorts by popularity of artist

            },

            url: "https://api.musixmatch.com/ws/1.1/track.search",
            dataType: "jsonp",
            jsonpCallback: 'jsonp_callback',
            contentType: 'application/json',
            success: function(data) {
                var trackResults = data.message.body.track_list;
                resultsSection.innerHTML += `<thead>
                                                <tr>
                                                  <th scope="col">Track Name</th>
                                                  <th scope="col">Artist</th>
                                                  <th scope="col">Lyrics</th>
                                                </tr>
                                             </thead>`;
                trackResults.forEach(function(item) {
                    resultsSection.innerHTML += `<tbody>
                                                    <tr>
                                                        <td>${item.track.track_name}</td>
                                                        <td>${item.track.artist_name}</td>
                                                        <td>
                                                            <button class="btn-result" onclick="returnLyrics(${item.track.track_id}, 'getTrack')">Lyrics</button>
                                                        </td>
                                                    </tr>
                                                </tbody>`;

                });
                if (trackResults.length === 0) {
                    resetPage(); //necessary to clear the table header already printed above.
                    resultsSection.innerHTML += `<thead>
                                                    <tr>
                                                        <th scope="col">A problem has occurred</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td>Sorry, no results were found.</td>
                                                    </tr>
                                                </tbody>`;
                }


            },

        }

    );
}

//If 'artist' radio button is selected:
function getArtist() {
    resetPage();
    $.ajax({
            type: "GET",
            data: {
                apikey: "16099f064260947071709a4bc6421891",
                q_artist: searchTerms, //queries by artist name
                format: "jsonp",
                callback: "jsonp_callback",
                page_size: 50, //returns the top 50 results
                s_artist_rating: "DESC", //sorted by popularity of artist

            },

            url: "https://api.musixmatch.com/ws/1.1/artist.search",
            dataType: "jsonp",
            jsonpCallback: 'jsonp_callback',
            contentType: 'application/json',
            success: function(data) {
                var artistResults = data.message.body.artist_list;
                resultsSection.innerHTML += `<thead>
                                                <tr>
                                                  <th scope="col">Artist Name</th>
                                                  <th scope="col">Albums</th>
                                                </tr>
                                             </thead>`;
                artistResults.forEach(function(item) {
                    resultsSection.innerHTML += `<tbody>
                                                        <tr>
                                                        <td>${item.artist.artist_name}</td>
                                                        <td>
                                                            <button class="btn-result" onclick="getAlbumList(${item.artist.artist_id})">Albums</button>
                                                        </td>
                                                    </tr>
                                                </tbody>`;

                });
                if (artistResults.length === 0) {
                    resetPage(); //necessary to clear the table header already printed above.
                    resultsSection.innerHTML += `<thead>
                                                    <tr>
                                                        <th scope="col">A problem has occurred</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td>Sorry, no results were found.</td>
                                                    </tr>
                                                </tbody>`;
                }

            },

        }

    );
}


//If user opts to view an artist's albums via the getArtist function:
function getAlbumList(artistID) {
    window['currentArtist'] = artistID; //makes the artistID available to use with the Go Back button on the track list results (from getTrackList)(assistance from mentor CZ on this line)
    resetPage();
    $.ajax({
            type: "GET",
            data: {
                apikey: "16099f064260947071709a4bc6421891",
                artist_id: artistID, //unique ID of the specified artist
                format: "jsonp",
                callback: "jsonp_callback",
                page_size: 100, //returns the top 100 results
                g_album_name: 1 //groups albums of the same name into one result

            },
            url: "https://api.musixmatch.com/ws/1.1/artist.albums.get",
            dataType: "jsonp",
            jsonpCallback: 'jsonp_callback',
            contentType: 'application/json',
            success: function(data) {
                var albumList = data.message.body.album_list;
                backButton.innerHTML += `<button class="btn-back" style="width:35%" onclick="getArtist()">Back</button>`;
                resultsSection.innerHTML += `<thead>
                                                <tr>
                                                  <th scope="col">Album Name</th>
                                                  <th scope="col">Track List</th>
                                                </tr>
                                            </thead>`;
                albumList.forEach(function(item) {
                    resultsSection.innerHTML += `<tbody>
                                                    <tr>
                                                        <td>${item.album.album_name}</td>
                                                        <td>
                                                            <button class="btn-result" onclick="getTrackList(${item.album.album_id})">Tracks</button>
                                                        </td>
                                                    </tr>
                                                </tbody>`;
                });
                if (albumList.length === 0) {
                    resetPage(); //necessary to clear the table header already printed above.
                    backButton.innerHTML += `<button class="btn-back" style="width:35%" onclick="getArtist()">Back</button>`;
                    resultsSection.innerHTML += `<thead>
                                                    <tr>
                                                        <th scope="col">A problem has occurred</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td>Sorry, no results were found.</td>
                                                    </tr>
                                                </tbody>`;
                }




            }
        }

    );
}

//If user opts to view an album's tracks via the getAlbumList function:
function getTrackList(albumID) {
    window['currentAlbum'] = albumID; //makes the album ID available to use for the Go Back button on the lyrics page (returnLyrics)
    resetPage();
    $.ajax({
            type: "GET",
            data: {
                apikey: "16099f064260947071709a4bc6421891",
                album_id: albumID, //unique ID of the specified album
                format: "jsonp",
                callback: "jsonp_callback",
                page_size: 50, //returns the top 50 results

            },
            url: "https://api.musixmatch.com/ws/1.1/album.tracks.get",
            dataType: "jsonp",
            jsonpCallback: 'jsonp_callback',
            contentType: 'application/json',
            success: function(data) {
                var trackResults = data.message.body.track_list;
                backButton.innerHTML += '<button class="btn-back" style="width:35%" onclick="getAlbumList(' + window['currentArtist'] + ')">Back</button>';
                resultsSection.innerHTML += `<thead>
                                                <tr>
                                                  <th scope="col">Track Name</th>
                                                  <th scope="col">Lyrics</th>
                                                </tr>
                                             </thead>`;
                trackResults.forEach(function(item) {
                    resultsSection.innerHTML += `<tbody>
                                                    <tr>
                                                        <td>${item.track.track_name}</td>
                                                        <td>
                                                            <button class="btn-result" onclick="returnLyrics(${item.track.track_id}, 'getTrackList')">Lyrics</button>
                                                        </td>
                                                    </tr>
                                                </tbody>`;
                });
                if (trackResults.length === 0) {
                    resetPage(); //necessary to clear the table header already printed above.
                    backButton.innerHTML += '<button class="btn-back" style="width:35%" onclick="getAlbumList(' + window['currentArtist'] + ')">Back</button>';
                    resultsSection.innerHTML += `<thead>
                                                    <tr>
                                                        <th scope="col">A problem has occurred</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td>Sorry, no results were found.</td>
                                                    </tr>
                                                </tbody>`;
                }

            }
        }

    );
}

//when a song has been selected from the results in getTrackList or getTrack:
function returnLyrics(trackID, goBack) {
    resetPage();
    var trackName;

    function createBackButton() {
        if (goBack == 'getTrack') {
            backButton.innerHTML += '<button class="btn-back" style="width:35%" onclick="getTrack()">Back</button>';
        }
        else {
            backButton.innerHTML += '<button class="btn-back" style="width:35%" onclick="getTrackList(' + window['currentAlbum'] + ')">Back</button>';
        }
    }
    createBackButton();
    $.ajax({
        type: "GET",
        data: {
            apikey: "16099f064260947071709a4bc6421891",
            track_id: trackID, //unique ID of the song
            format: "jsonp",
            callback: "jsonp_callback",

        },
        url: "https://api.musixmatch.com/ws/1.1/track.get",
        dataType: "jsonp",
        jsonpCallback: 'jsonp_callback',
        contentType: 'application/json',
        success: function(data) {
            trackName = data.message.body.track.track_name; //creates a variable holding the name of the selected song for use in the table heading
        },
        complete: function() {
            $.ajax({
                type: "GET",
                data: {
                    apikey: "16099f064260947071709a4bc6421891",
                    track_id: trackID, //unique ID of the song
                    format: "jsonp",
                    callback: "jsonp_callback",

                },
                url: "https://api.musixmatch.com/ws/1.1/matcher.lyrics.get",
                dataType: "jsonp",
                jsonpCallback: 'jsonp_callback',
                contentType: 'application/json',
                success: function(data) {
                    try { //checks to make sure there are lyrics to return
                        var lyricResults = data.message.body.lyrics.lyrics_body;
                        var lyricCopyright = data.message.body.lyrics.lyrics_copyright;
                    }
                    catch (err) { //if there are no lyrics to return, an error is printed and the rest of the function is aborted
                        resultsSection.innerHTML += `<thead>
                                                <tr>
                                                  <th scope="col">A problem has occurred</th>
                                                </tr>
                                             </thead>
                                             <tbody>
                                                <tr>
                                                    <td>Sorry, there are no lyrics available for this song.</td>
                                                </tr>
                                             </tbody>`;
                        return;

                    }
                    //lyrics are printed into the results div.
                    resultsSection.innerHTML += `<thead> 
                                                <tr>
                                                  <th scope="col">${trackName}</th>
                                                </tr>
                                             </thead>
                                             <tbody>
                                                <tr>
                                                    <td class="lyrics">${lyricResults}<br>${lyricCopyright}</td>
                                                </tr>
                                             </tbody>`;

                    if (lyricResults == "" && lyricCopyright == "") {
                        resetPage();
                        createBackButton();
                        resultsSection.innerHTML += `<thead>
                                                <tr>
                                                  <th scope="col">A problem has occurred</th>
                                                </tr>
                                             </thead>
                                             <tbody>
                                                <tr>
                                                    <td>Sorry, there are no lyrics available for this song.</td>
                                                </tr>
                                             </tbody>`;
                        return;
                    }
                }
            });
        }
    });
}
