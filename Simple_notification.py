from gi.repository import Notify
Notify.init("TimeTable")
summary = "Wake Up!"
body = "Online School Starts At 7 o' clock!"
Notify.Notification.new(summary, body,).show()
     