# TikTokToBlueSkyFollowerTransfer
 Attempts to transfer a users followers from TikTok to BlueSky by username


# How To Use
After downloading your TikTok information as a json file from the app, unzip the and move the json file anywhere you would like.

Next move 'TikTokToBlueSkyFollowerTransfer.exe' from inside the 'dist' folder, into the same folder as that json file.

Right click in the File Explorer Application of your choice, and click 'Open In Terminal'. This should be universal for any standard desktop operating system.

Once the console is open, for Windows type out ".\TikTokToBlueSkyFollowerTransfer.exe" without the quotations. For Linux and Mac, it should be "./TikTokToBlueSkyFollowerTransfer.exe", again with no quotataions.

Add a space after this, and enter your full BlueSky username. The default username ends in ".bsky.social". Add another space, and enter your BlueSky password, and press "Enter" or "Return".

The program will begin, and you can watch to see which usernames were found, and which were not. Your account will automatically follow these found accounts.

# For those worried about entering your password...
I invite you to review the code and see that nothing is done with the credentials the user enters, other than logging in to allow the automatic following.

For those who may not be able to read or understand a programming language like this, I invite you to google how to do a 'check sum' on a file, and perform it on the 'exe' file.

you can then compare it to the checksum in 'checksum.txt' and you will see they are the same, indicating the 'exe' file has not been modified in any way, and is safe to use.
