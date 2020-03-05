This visualization was created with [gource](https://gource.io/), which is normally used to visualize the development of software projects, like [here](https://www.youtube.com/watch?v=MkJxlKD2bjk).

I wrote a Python script that uses [PRAW](https://praw.readthedocs.io/en/latest/), the Python Reddit API Wrapper to retrieve the 25 hottest submissions, traverses their comments and writes them to a file, in the [Log Format](https://github.com/acaudwell/Gource/wiki/Custom-Log-Format) that gource accepts.

After that, I started gource in --fullscreen mode and used [OBS](https://obsproject.com/) to record the video.

You can find the script here: https://github.com/void4/reddgource
Video link: https://streamable.com/4ik8w
