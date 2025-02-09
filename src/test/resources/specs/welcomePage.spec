@import common.spec

@objects
    welcome-block       css     .jumbotron
    greeting            css     #welcome-page h1
    text-block-*        css     #welcome-page p
    login-button        css     #welcome-page .button-login



= Content =
    @on *
        text-block-1, login-button, text-block-3:
            inside welcome-block ~30px left

        greeting:
            above text-block-1 5 to 10 px
            inside welcome-block ~ 30px left

        text-block-1:
            height > 20px

        login-button:
            height ~ 45px
            text is "Login"


    @on desktop
        greeting:
            height ~ 69px
            inside welcome-block ~ 68 px top

        text-block-1:
             above login-button 60px

        login-button:
            width ~ 78px


    @on tablet
        greeting:
            height ~ 39px
            inside welcome-block ~ 50 px top

        text-block-1:
             above login-button 90px

        login-button:
            width ~ 78px

    @on mobile
        greeting:
            height ~ 78px
            inside welcome-block ~ 50 px top

        text-block-1:
             above login-button 130px

        login-button:
            inside welcome-block ~ 30px left right
