<header>
    <h1>Menu</h1>
</header>

<hr>
<br>

<main>
    <nav>
        <ul>
            <?php
                $array = array('Reserva','Usuario','Salas');
                // for($a = 0; $a <= (sizeof($array)-1); $a++){
                //     echo "<li> $array[$a] </li>";
                // }

                foreach($array as $tes){
                    echo "<li> $tes </li>";
                }
            ?>
        </ul>
    </nav>
</main>


