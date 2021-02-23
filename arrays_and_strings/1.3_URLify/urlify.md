## URLify

This solution first declares a new character array to hold the URLified string. This is the same size as the character array holding the orginal string.  
It then iterates over the start of the original string to where the padding spaces begin. It also sets an index counter to zero.
Each character is copied over to the new array at the position of the counter - if the character is a space, the URL characters are written over it and the counter is incremented by 3 to account for this.

This implentation takes n time because it iterates through the length of the string.