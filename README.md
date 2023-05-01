# ✍ Nebula-16-Programmazione-Sicura

This challenge is another variation of command injection exploit. The web service is running on port **1616**, and the source code is provided to us for reference. We can use netcat to connect to this service.

The username parameter is something we control, and will be the point for command injection. To exploit this level we could escape the egrep command by using a backtick to inject a bash command such as “`ls -aril`” within the supplied username parameter. This should lead to arbitrary code execution — but there is a problem, the exploit is being passed to an uppercase filter which will cause any exploit or injection to fail (Sadly, linux is case sensitive, this would have worked on a Windows OS)

The way to bypass this is to exploit the bash wildcard expansion: 
1. We can create an exploit and place it in */tmp/* folder where both the **level16** and **flag16** users have read and write access to. 
2. We can name our exploit file in all caps or numbers(eg A123BCD). When we supply the username parameter like /*/A123BCD the uppercase won’t affect it, and the bash wildcard will find only 1 file which is our exploit in /tmp/ that matches the pattern. 
3. Inside the exploit we can place a reverse shell to our machine and execute **getflag**.

# 🏁 How to use

### 📥 Download Nebula
You can download Nebula [here](https://exploit.education/downloads/).

### 📍 How to start
Log in to the virtual machine as **username** "levelXX" with a **password** of "levelXX" (without quotes), where XX is the level number. Some levels can be done purely remotely.

### 🩺 Get Root permissions (optional)
In case you need root access to change things (like key mappings, etc.), then you can log in with the following credentials:
* **Username** = "nebula" 
* **Password** = "nebula".

Then you need to type "sudo -s" and you will then have root privileges to change what needs.

### 📝 Source code
The source code can be viewed [here](https://github.com/xzan8189/Nebula-16-Programmazione-Sicura/)
