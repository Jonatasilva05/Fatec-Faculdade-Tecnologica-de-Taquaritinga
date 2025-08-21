<?php
    require "style.php"
?>

<header>
    <h1>
        Atividade - Aula conceitos PHP - 23/08/2024
    </h1>
    <a href="">Link repositório do GitHub</a>
</header>

<main class="container">
    <div class="modulo">
        <div class="card1">
            <h2>1. Estamos aprendendo PHP!</h2>
            <section>
                <p class="phpDiv">
                    <?php
                        echo "Vamos prosseguir aprendendo PHP";
                    ?>
                </p>
                <p>
                    <span>Listagem 1</span>. Exemplo de uso do <span>PHP</span>(index.php)
                </p>
                <p>
                    O arquivo index foi salvo com a extensão .php para mostrarmos ao nosso interpretador que há um código <span>PHP</span> a ser interpretado. Além disso, no exemplo usamos a função <span class="echoSpan">echo</span> para escrever na tela uma mensagem.
                </p>
            </section>
        </div>

        <section>
            <h2>Como comentar o código no PHP</h2>
            <p>
                Para comentarmos o nosso <span>PHP</span> usamos duas barras ou # para comentários de uma linha, e para comentários de múltiplas linhas usamos /**/, o mesmo usado no CSS. Observe alguns exemplos na <span>Listagem 2.</span>
            </p>
        </section>

        <div class="card2">
            <section>
                <p class="phpDiv">
                    <?php
                        echo "Oi, Eu serei visto na sua tela";
                        //Eu não! Sou apenas um comentário.

                        echo "<br>";

                        echo "Oi, Eu também serei visto por você";
                        #Já eu não serei!

                        echo "<br>";

                        echo "E eu aqui novamente na sua tela, rs";
                        /*Eu não aparecerei na sua tela novamente pois sou um comentário*/
                    ?>
                </p>
            </section>
        </div>

        <section>
            <h2>Variáveis no PHP</h2>
            <p>
                Para criarmos uma variável basta ultilizar o sinal de cifrão. Uma variável pode armazenar textos e números. Além disso, a linguagem PHP é case sensitive, então A é diferente de a. Observe um exemplo de uso de variáveis na <span>Listagem 3.</span>
            </p>
        </section>

        <div class="card3">
            <section>
                <p class="phpDiv">
                    <?php
                        $name = "Guilherme";
                        $age = 20;

                        echo $name; //Guilherme
                        echo "<br>";
                        echo $age; //20
                    ?>
                </p>
            </section>
        </div>

        <section>
            <p>
                No exemplo criamos uma variável <span class="echoSpan">$name</span> e declaramos a ela uma string, sendo assim precisamos colocá-la entre aspas. Já a outra variável <span class="echoSpan">$age</span> é declarada como inteiro, então não é necessário o uso de aspas. Ao usarmos o comando <span class="echoSpan">echo</span> nas variáveis, o resultado impresso é o conteúdo dessa variável.
            </p>
            <p>
                Para a nomeação de variáveis, as dicas a seguir são necessárias:
            </p>

            <ul>
                <li>Não inicie o nome de uma variável com números;</li>
                <li>Não ultilize espaços em brancos;</li>
                <li>Não ultilize caracteres especiais, somente underline;</li>
                <li>Crie variáveis com nomes que ajudarão a identificar melhor a mesma;</li>
                <li>Evite ultilizar letras maiúsculas.</li>
            </ul>

            <p>
                Falaremos agora sobre alguns dos tipos de variáveis que existem no <span>PHP:</span>
            </p>

            <ul>
                <li><span>Booleanos:</span>Este é o tipo mais simples, pois só pode expressar apenas dois valores: <span>TRUE(1)</span> ou <span>FALSE(0, null ou uma string vazia);</span></li>
                <li><span>Integer:</span>é um numero inteiro, podendo ser negativo ou positivo;</li>
                <li><span>Float:</span>também chamado de double ou numeros reais representados com um ponto para separar os dígitos do valor das casas decimais.</li>
                <li><span>Strings:</span>é uma palavra ou frase entre aspas ou duplas, assim como também pode ser binário, como o conteúdo de um arquivo MP3 ou JPG. Veja os exemplos na <span>Listagem 4.</span></li>
            </ul>
        </section>

        <div class="card4">
            <p class="phpDiv">
                <?php
                    $a = "mundo!";
                    echo "Olá, $a"; //Olá, mundo!
                    echo 'Olá, $a'; //Olá, $a
                ?>
            </p>
        </div>

        <section>
            <p>
                Note que quando declaramos no <span class="echoSpan">echo 'Olá, $a';</span>, o PHP interpretou o conteúdo da variável <span class="echoSpan">$a'</span>, pois está entre aspas duplas. E quando usamos a mesma forma, só que entre aspas simples <span class="echoSpan">echo 'Olá, $a';</span>, não temos o mesmo resultado.
            </p>
            <p>
                Então quando queremos que o PHP interprete o valor de nossa dentro de uma string é necessário o uso de aspas duplas.
            </p>
            <p>
                Além disso, podemos usar umm ponto para concatenar strings, assim como o sinal + JavaScript, como mostra o código da <span>Listagem 5.</span>
            </p>
        </section>

        <div class="card5">
            <section>
                <p class="phpDiv">
                    <?php
                        echo "Olá," . "mundo!";
                        //Olá, mundo!
                    ?>
                </p>
            </section>
        </div>

        <section>
            <h2>Constantes no PHP</h2>
            <p>
                O valor de uma constante jamais poderá ser alterado enquanto estiver executada e para defini-la ultilizamos a função <span class="spanItalic">define()</span> ou <span class="spanItalic">const</span>, como mostra a <span>Listagem 6.</span>
            </p>
        </section>

        <div class="card6">
            <section>
                <p class="phpDiv">
                    <?php
                        define("PHP", "Linguagem Open - Source");

                        const HTML = "Linguagem de marcação";

                        echo PHP; //Linguagem Open - Souce

                        echo HTML; //Linguagem de marcação
                    ?>
                </p>
            </section>
        </div>

        <section>
            <p>Ultilizando a função <span class="echoSpan">define()</span> ou a palavra reservada <span class="echoSpan">const</span> definimos que as constantes com os nommes de PHP e HTML respectivamente, com o valor:Linguagem Open - Source e Linguagem de marcação.</p>

            <h2>Arrays no PHP</h2>

            <p>
                um <span class="spanItalic">array</span> que mantém uma série de elementos que podem ter diferentes tipos, como mostra a <span>Listagem 7.</span>
            </p>
        </section>

        <div class="card7">
            <p class="phpDiv">
                <?php
                    $php = array("Zend" => "CERTIFICAÇÃO", 6 => false);
                    echo $php["Zend"]; //CERTIFICAÇÃO
                    echo $php[6]; //0

                    //Zend é nossa chave e CERTIFICAÇÃO nosso valor
                    // 6 é nossa chave e false(0) é nosso valor
                ?>
            </p>
        </div>

        <section>
            <p>
                Note que nossa primeira chave se chama Zend, e a outra chama-se 6, mas quanto a nomeação de chaves de array pode ser tanto string ou um interger.Para o valor pode ser qualquer coisa.
            </p>

            <h2>Conversão de tipos</h2>

            <p>Os tipos de <span class="spanList">variáveis no PHP</span> são dinâmicos. Para forçarmos os tipos de nossas variáveis ultilizamos uma técnica conhecida como type casting, ou simplesmente troca de tipos. Veja na <span>Listagem 8</span> alguns exemplos</p>
        </section>

        <div class="card8">
            <p class="phpDiv">
                <?php
                    $var = 100;
                    $type_casting = (bool) $var;
                    $type_casting = (int) $var;
                    $type_casting = (float) $var;
                    $type_casting = (string) $var;
                    $type_casting = (array) $var;
                    echo $type_casting = (bool) $var;
                ?>
            </p>
        </div>

        <section>
            <p>Veja que transformamos o valor da <span class="echoSpan">$var</span>, que antes era um inteiro, para umm valor booleano.
            </p>
            <p>
                Vamos conhecer agora <span>operadores</span>, que permitem que nós manipulemos o conteúdo de uma ou mais variáveis.
            </p>

            <h2>Operadores Aritméticos no PHP</h2>

            <p>
                Podemos ultilizar operadores matemáticos para efetuar cálculos com os valores de variáveis, como mostra a <span>Listagem 9.</span>
            </p>
        </section>

        <div class="card9">
            <p class="phpDiv">
                <?php
                    $a = 3;
                    $b = 3;
                    $c = $a * $b; //resultado é 9
                    $d = $a + $b; //resultado é 6
                    $e = $c - $d; //resultado é 3
                ?>
            </p>
        </div>

        <section>
            <p>
                Criamos as variáveis <span class="echoSpan">$a</span> e <span class="echoSpan">$b</span> e a partir delas conseguimos fazer vários cálculos matemáticos.
            </p>

            <p>
                Os operadores matemáticos disponíveis em PHP são:
            </p>

            <ul>
                <li>Adição:+</li>
                <li>Subtração:-</li>
                <li>Multiplicação:*</li>
                <li>Divisão:/</li>
                <li>Módulo:%</li>
            </ul>

            <p>
                Lembrando que não precisamos especificar os tipos de variáveis no PHP, como nos exemplos a seguir:
            </p>
        </section>

        <div class="card10">
            <p class="phpDiv">
                <?php
                    $a = "5"; //string
                    echo $a + 2; // 7, integer
                    echo $a + '5 carros'; // 10, integer
                ?>
            </p>
        </div>

        <section>
            <p>
                Note que <span class="echoSpan">$a</span> é uma string e quando demos um <span class="echoSpan">echo</span> nela somando com 2, que é um inteiro, o resultado retornado foi 7. Isso demonstra que nossos tipos de variáveis em PHP são sempre dinâmicos. E na linha 4 o PHP reconhece dentro das aspas simples um numeral e com isso executa a operação matemática e exibirá o resultado de 10 do tipo inteiro mas não exibindo a palavra "carros".
            </p>

            <h2>Operadores de Atribuição no PHP</h2>

            <p>
                Ultilizamos os operadores de atribuição para definir variáveis e seus valores, além de usá-los juntamente com os operadores matemáticos, como mostra o exemplo da <span>Listagem 10.</span>
            </p>
        </section>

        <div class="card11">
            <p class="phpDiv">
                <?php
                    $a = 1; // A variavel $a é igual a 1
                    $a += 2; // Somamos 2 ao valor da $a;
                    echo $a;
                ?>
            </p>
        </div>

        <section>
            <p>
                O resultado acima é 3, pois somamos 2 ao valor da <span class="echoSpan">$a</span>, que é 1. Na <span>Listagem 11</span> temos mais exemplos.
            </p>
        </section>

        <div class="card12">
            <p class="phpDiv">
                <?php
                    $a -= 2;
                    $a *= 2;
                    $a /= 2;
                ?>
            </p>
        </div>

        <section>
            <p>
                A sintaxe desses operadores é a mesma do exemplo da soma, pois basta dar echo depois de ter declarado a variável com seu respectivo operador.
            </p>

            <p>
                Podemos também incrementar ou decrementar variáveis ultilizando os operadores de incrementação, herdados da linguagem C, como nos exemplos da <span>Listagem 12.</span>
            </p>
        </section>

        <div class="card13">
            <p class="phpDiv">
                <?php
                    $a = 1;
                    echo ++$a;
                    echo $a++;
                    echo --$a;
                    echo $a--;
                ?>
            </p>
        </div>

        <section>

            <h2>Operadores Relacionais</h2>

            <p>
                Esses são usados para comparar valores ou expressões, retornando um valor booleano (true ou false):
            </p>

            <ul>
                <li>Igual: ==</li>
                <li>Idêntico: ===</li>
                <li>Diferente: != ou <></li>
                <li>Menor que: <</li>
                <li>Maior que: ></li>
                <li>Menor ou Igual: <=</li>
                <li>Maior ou igual: >=</li>
            </ul>

            <p>
                É importante lembrar que == não checa o tipo da variavel, apenas seu valor. Já o <span class="echoSpan">===</span> checa  tanto o valor da variável quanto o seu tipo.
            </p>

            <h2>Operadores Lógicos</h2>

            <p>
                Existem também os operadores lógicos para a criação de testes condicionais:
            </p>

            <ul>
                <li>$a and $b: enquanto A e B forem verdadeiros</li>
                <li>$a or $b: enquanto A e B forem verdadeiros</li>
                <li>$a xor $b: enquanto A e B forem verdadeiros, mas não os dois</li>
                <li>!$a: verdadeiro se A for falso;</li>
                <li>$a || $b: enquanto A ou B forem verdadeiros.</li>
            </ul>

            <h2>Estrutura de Decisão if/else</h2>

            <p>
                A condição é avaliada para que, caso algo seja verdadeiro, faça isto,senão, faça aquilo, como mostra a <span>Listagem 13.</span>
            </p>
        </section>

        <div class="card14">
            <p class="phpDiv">
                <?php
                    $idade = 17;

                    if($idade < 18) {
                        echo 'Você não pode entrar aqui!';
                    } else {
                        echo 'Seja bem - vindo';
                    }
                ?>
            </p>
        </div>

        <br><br>

        <div class="card15">
            <p class="phpDiv">
                <?php
                    $idade = 21;
                    $identidade = true;

                    if($idade > 18 && $identidade == true) {
                        echo 'Seja bem-vindo';
                    }
                ?>
            </p>
        </div>

        <br><br>

        <div class="card16">
            <p class="phpDiv">
                <?php
                    $nome = 'Till Lindemann';

                    if($nome == 'Richard Kruspe') {
                        echo 'E ae Richard Kruspe!';
                    } elseif ($nome == 'Oliver Riedel') {
                        echo 'E ae Oliver Riedel!';
                    } elseif ($nome == 'Till Lindemann') {
                        echo 'E ae Till Lindemann!';
                    } else {
                        echo "E ae $nome!";
                    }
                ?>
            </p>
        </div>

        <br><br>

        <div class="card17">
            <p class="phpDiv">
                <?php
                    $nome = 'Fulano';

                    switch ($nome) {
                        case 'Fulano':
                            echo 'E ai Fulano';
                            break;

                        case 'Sicrano':
                            echo 'E ai Sicrano';
                            break;

                        case 'Beltrano':
                            echo 'E ai Beltrano';
                            break;

                        default:
                            echo 'Qual é o seu nome';
                            break;
                    }

                    //Resultado é: E ai Fulano!
                ?>
            </p>
        </div>

        <br><br>

        <div class="card18">
            <p class="phpDiv">
                <?php
                    $number1 = 1;
                    $number2 = 2;

                    if($number1 > $number2) {
                        $a = 'Numero 2 é maior que número 1';
                    } else {
                        $b = 'Numero 2 não é maior que número 1';
                    }

                    $ternario = ($number2 > $number1) ? 'Numero 2 é maior que número 1' : 'Numero 2 não é maior que número 1';

                    echo $ternario; //Numero 2 é maior que número 1
                ?>
            </p>
        </div>

        <br><br>

        <div class="card19">
            <p>
                <?php
                    $estacao = array('Verao' => 'de 21 de dezembro a 21 de março',
                    'Outono' => 'de 21 de março a 21 de junho',
                    'Inverno'=> 'de 21 de junho a 23 de setembro',
                    'Primavera'=> 'de 23 de setembro a 21 de dezembro');
                ?>
            </p>
        </div>

        <br><br>


        




    </div>
</main>