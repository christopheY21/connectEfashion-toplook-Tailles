grammar toplookSizes;

sizes : size + ('+' size)*;
size : INT '=' sizeformat;
sizeformat : 'XS'
            | 'S'
            | 'M'
            | 'L'
            | 'XL'
            | 'XXL';
INT : [0-9]+ ; 
WS : [ \t\r\n]+ -> skip ;
