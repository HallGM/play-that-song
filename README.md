# What is it?

**Play That Song** is a song request app for DJs and club venues. The app has two user interfaces - the screen that the DJ sees, and the screen that the attendee of the event sees. The attendees can log in through their mobile devices to request a song, which will then appear on the screen of the DJ’s device.

# How to use

## DJ Interface

![DJ interface](./screenshots/dj_view.png?raw=true "Dj View")

The first page and the main page that you are greeted with is the DJ _request_ page. Incoming requests will appear in blue, and once you check them off, they will appear on the grey _played_ list

As the DJ, you can add, edit and delete user profiles in the _Users_ page. You can also add edit and delete songs in the _Songs_ page. Run a

## Switching to attendee interface mode

In the users page, click on one of the users and this will take you to their user profile. From here, click _use app as this user_ to see the device from this user's perspective.
(This is not an intended feature, and just here to simulate a user logging into the app)

## Attendee Interface

This part of the user interface is optimized for mobile users. Users can request a song, see a list of all songs that have been played, or se a list of all songs that they have requested.

![Attendee interface](./screenshots/attendee_view.png?raw=true "Attendee Mobile View")

To request a song, type either the name of the song or the artist into the _search_ bar.

![Attendee interface Search Bar](./screenshots/attendee_view_search.png?raw=true "Attendee Mobile View Search")

# About

This project was created in **Python**, using **Flask**, **Psycopg**, **PostgreSQL**, **Jinja**, and **SASS**
