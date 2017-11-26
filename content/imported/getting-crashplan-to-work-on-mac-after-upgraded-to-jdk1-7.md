Title: Getting #CrashPlan to work on #Mac after upgraded to JDK1.7
Date: 2012-11-09 17:10
Author: masayukig
Tags: crashplan, Mac
Status: published

I got an error of CrashPlan a few days ago. That is
<https://gist.github.com/4046875.js?file=engine_error.log> So CrashPlan
did not work from the day. I sought to resolve this problem and [found
it](http://java.dzone.com/articles/getting-crashplan-work-mac). Modify
the "/Library/LaunchDaemons/com.crashplan.engine.plist"
<https://gist.github.com/4046875.js?file=com.crashplan.engine.plist.diff>
And, <https://gist.github.com/4046875.js?file=reload_crashplan.sh>
That's it.
