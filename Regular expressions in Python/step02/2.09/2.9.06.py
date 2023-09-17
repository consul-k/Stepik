'''

Напишите регулярное выражение, которое найдёт все теги img в тексте.

Что нужно найти:

Нужно найти последовательности, подходящие по следующим условиям:

    Начинается с <img
    Заканчивается на >
    Между началом и концом могут находиться последовательности из любых символов

Sample Input 1:

<picture><source srcset="/static/frontend/new-year/2022/topbar_logo_small.svg" media="(max-width: 1024px)"><img class="navbar__logo" alt="Stepik" src="/static/frontend/new-year/2022/topbar_logo.svg"></picture>

Sample Output 1:

<img class="navbar__logo" alt="Stepik" src="/static/frontend/new-year/2022/topbar_logo.svg">

Sample Input 2:

<button class="navbar__profile-toggler st-button_style_none" aria-label="Profile" aria-describedby="profile-notifications-badge platform-news-badge" type="button"><img class="navbar__profile-img" alt="User avatar" src="https://stepik.org/media/users/287786858/avatar.png?1665242572"><div class="new-year-navbar-avatar" data-drawn="2933"></div><span id="profile-notifications-badge" class="navbar__profile-notifications-badge" aria-label="0 notifications" data-count="0">0</span><span id="platform-news-badge" class="navbar__profile-news-badge platform-news-badge" aria-label="You have unread platform news"></span></button>

Sample Output 2:

<img class="navbar__profile-img" alt="User avatar" src="https://stepik.org/media/users/287786858/avatar.png?1665242572">

Sample Input 3:

<img src="smiley.gif" alt="Smiley face" width="42" height="42" style="vertical-align:bottom"><img src="smiley.gif" alt="Smiley face" width="42" height="42" style="vertical-align:middle"><img src="smiley.gif" alt="Smiley face" width="42" height="42" style="vertical-align:top"><img src="smiley.gif" alt="Smiley face" width="42" height="42" style="float:right"><img src="smiley.gif" alt="Smiley face" width="42" height="42" style="float:left"> 

Sample Output 3:

<img src="smiley.gif" alt="Smiley face" width="42" height="42" style="vertical-align:bottom"> <img src="smiley.gif" alt="Smiley face" width="42" height="42" style="vertical-align:middle"> <img src="smiley.gif" alt="Smiley face" width="42" height="42" style="vertical-align:top"> <img src="smiley.gif" alt="Smiley face" width="42" height="42" style="float:right"> <img src="smiley.gif" alt="Smiley face" width="42" height="42" style="float:left">

Sample Input 4:

<img>

Sample Output 4:

<img>

'''

regex = r'<img.*?>'
