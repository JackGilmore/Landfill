---
layout: default
title: "Home"
---

<p>An archive of the Trash Compactor/Fantastic Beats playlist</p>

{% assign playlists = site.data.playlists | sort %}
{% for playlist in playlists %}
{% assign playlist_date = playlist[0] | split: "_" | first %}

<h2 >{{playlist_date}} {{playlist.url}}</h2>
<table class="table table-bordered table-striped">
    <thead>
        <tr>
            <th>Title</th>
            <th>Artist</th>
            <th>Added by</th>
        </tr>
    </thead>
    <tbody>
    {% assign playlist_tracks = playlist[1] %}
    {% for track in playlist_tracks %}
        <tr>
            <td>{{track.track.name}}</td>
            <td>{{track.track.artists | map: "name" | join: ", " }}</td>
            <td>{{site.data.usermap[track.added_by.id]}}</td>
        </tr>
    {% endfor %}
    </tbody>
</table>
{% endfor %}
