# morse-encoder
Console-based application for translating English text into Morse Code script.

<h1>How it works</h1>
<p>The program contains a dictionary of English letters and symbols and their Morse Code equivalents. Upon user input
each character is run through the dictionary to create a list of Morse Code characters, which is joined together as a
string and printed. If the character is not found (i.e. it raises a KeyError), the user is informed of which character
in their string can't be translated by returning the character in an f-string:</p>
<p><em>except KeyError as e:</em></p>
<p><em>&nbsp;&nbsp;print(f"The character '{e.args[0]}' is not an option for translating into Morse Code.")</em></p>