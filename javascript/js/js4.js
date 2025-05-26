let x=0;
        function count() {
            
            x++;
            document.querySelector('h2').innerHTML = x;
            if (x % 10 === 0) {
                document.querySelector('h2').style.color = 'blue';
                alert(`Count: ${x}`);
            } else {
                document.querySelector('h2').style.color = 'red';
            }
            
        }
        
        // document.querySelector('button').onclick = count;
        document.addEventListener('DOMContentLoaded', function() {
            //document.querySelector('button').addEventListener('click', count);
            document.querySelector('button').onclick=count
        });
