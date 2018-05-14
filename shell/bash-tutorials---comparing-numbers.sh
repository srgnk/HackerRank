read x
read y

(( $x > $y )) && echo 'X is greater than Y'
(( $x < $y )) && echo 'X is less than Y'
(( $x == $y )) && echo 'X is equal to Y'