#Cross Platform Mobile Apps
The app written here are the very basic sketch on how you can use Apache Cordova to build iOS,Android,Windows,etc. application for your IOT project.

## Usage
###Install Cordova on your system
Follow the [link](http://cordova.apache.org/docs/en/5.0.0/guide_cli_index.md.html) to get it up and running.
Again, Linux and Mac commandline are super duper easy to work with.
###Install Ant on your system to build Android Application
You will need to install Apache Ant in your system. You could follow [this](http://ant.apache.org/)for more info on that.
###Install Android Studio
Follow this [link](https://developer.android.com/sdk/index.html) for that.
### For iOS
You will need a developer account and all that for a Mac. But just to emulate the entire thing, you will need to intsall XCODE. But then again , if you have been using the command line tools on Mac, you would have already done that.

####Quick sneak peak into how to start
Create `$ cordova create hello hello.sample.com HelloWorld`

Get in the directory and add platform
```
$ cd hello
$ cordova add platform android 
$ cordova build 
```
The above can be done for ios, android,fire-fox etc. To remove `$ cordova platform remove ios`

[Here](https://cordova.apache.org/docs/en/4.0.0/guide_cli_index.md.html) are more CLIs for Cordova.

## Questions?
But why not use something like MIT App Inventor?
>Well ofcourse you can, it is good to build an app using it if it is going to be for fun, not when you are trying to build a product. You can not scale an application written in MIT App Inventor.
>Need less to say you can not even use it to make an iOS app. The UI sucks. You can't really build anything which has a super intutive UI without hitting your head in the screen a few too many times.
>This is coming from a guy who was using MIT App Inventor to build apps till last year. That is when I discovered the beauty of Cordova and frameworks like Ionic(?). Don't worry it will all come to you so>on.
