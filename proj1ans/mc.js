        function setfocus() {
            document.getElementById('input').focus();
        }

        function clearnow() {
            document.getElementById('input').value = "";
            document.getElementById('output').value = "";
            location.reload();
        }

        function mc2c() {
            var ans = "";
            var mc2c = {'.-': 'A', '-...': 'B', '-.-.': 'C',
            '-..': 'D', '.': 'E', '..-.': 'F',
            '--.': 'G', '....': 'H', '..': 'I',  
            '.---': 'J', '-.-': 'K', '.-..': 'L',
            '--': 'M', '-.': 'N', '---': 'O', 
            '.--.': 'P', '--.-': 'Q', '.-.': 'R',
            '...': 'S', '-': 'T', '..-': 'U', 
            '...-': 'V', '.--': 'W', '-..-': 'X',
            '-.--': 'Y', '--..': 'Z', '-----': '0', 
            '.----': '1', '..---': '2', '...--': '3',
            '....-': '4', '.....': '5', '-....': '6', 
            '--...': '7', '---..': '8', '----.': '9',
            '--..--':',', '.-.-.-':'.', '..--..':'?',
            '-..-.':'/', '-....-':'-', '-.--.':'(',
            '-.--.-':')', '|':' ', ' ':''};

	    // Your code below

            var t = document.getElementById('input').value.toString().trim();
            var t1 = t.split(' ');
            for (var i=0; i < t1.length; i++){
                ans+=mc2c[t1[i].toString()];
            }
            /* */
            document.getElementById('output').innerHTML = ans.toString();
        }

        function c2mc() {
            var ans = "";
            var c2mc = { 'A':'.-', 'B':'-...', 
              'C':'-.-.' , 'D':'-..', 'E':'.', 
              'F':'..-.', 'G':'--.', 'H':'....', 
              'I':'..', 'J':'.---', 'K':'-.-', 
              'L':'.-..', 'M':'--', 'N':'-.', 
              'O':'---', 'P':'.--.', 'Q':'--.-', 
              'R':'.-.', 'S':'...', 'T':'-', 
              'U':'..-', 'V':'...-', 'W':'.--', 
              'X':'-..-', 'Y':'-.--', 'Z':'--..', 
              '1':'.----', '2':'..---', '3':'...--', 
              '4':'....-', '5':'.....', '6':'-....', 
              '7':'--...', '8':'---..', '9':'----.', 
              '0':'-----', ', ':'--..--', '.':'.-.-.-', 
              '?':'..--..', '/':'-..-.', '-':'-....-', 
              '(':'-.--.', ')':'-.--.-', ' ':'|'};

	    // Your code below

            var t = document.getElementById('input').value.toString().trim();
            t =  t.toUpperCase();

            for (var i=0; i < t.length; i++){
                ans+=c2mc[t.charAt(i)] + " ";
            }
            /* */
            document.getElementById('output').innerHTML = ans.toString();

        }