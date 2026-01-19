# TheySayThat - Universal Randomizer Hint Display

<img src="https://repository-images.githubusercontent.com/604310317/cf022e6e-d2d5-4318-8011-b4c5d541fb4c"  width="882" height="441">

They say that given a spoiler log from one of several popular randomizers, this program allows you to output the contents of hints you've discovered during a playthrough to a text file. If that file is then read by streaming software (perhaps using [StreamTicker](https://github.com/go1den/streamticker), for example), it can be displayed on stream in real time, allowing viewers to know all the hints you've received so far.

**Supported Randomizers:**  
[The Legend of Zelda: Ocarina of Time (v8.0)](https://ootrandomizer.com/)  
[The Legend of Zelda: Majora's Mask  (v1.15.2.1)](https://github.com/ZoeyZolotova/mm-rando/releases/tag/v1.15.2.1)  
[Donkey Kong 64 (v3.0)](https://dk64randomizer.com/)    
[Metroid Prime](https://randovania.github.io/)  

TheySayThat is designed to be a universal tool for hint display. Adding a new randomizer into the program requires only a simple class definition and, optionally, images for the buttons.
The only major requirement is that supported games must have a spoiler log that can be consistently parsed to obtain the hint information.

If you know of a randomizer that is not covered by TheySayThat, but that DOES have hint information stored in its spoiler logs, please contact me and I will add it.

If you want your favorite randomizer to support TheySayThat, please let the developers of that randomizer know that their spoiler logs need to contain hint information!

![TheySayThat](https://github.com/Go1den/TheySayThat/blob/main/example3.png?raw=true)

![TheySayThat2](https://github.com/Go1den/TheySayThat/blob/main/example2.png?raw=true)

![TheySayThat3](https://github.com/Go1den/TheySayThat/blob/main/example4.png?raw=true)

Note: This has only been tested on Windows 10. Try it elsewhere at your own risk.
