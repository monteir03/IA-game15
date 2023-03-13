    Linguagem Python 3
    Python 3.0
    Para executar os diferentes algoritmos o código deve ser invocado da seguinte maneira:

        code <strategy> < config

    onde "code" é a forma de invocar o seu código (nome de executável ou outra forma), "<strategy>" poderá ser uma de "DFS", "BFS", "IDFS", "A*-misplaced", "A*-Manhattan, "Greedy-misplaced", "Greedy-Manhattan" e "config" é um ficheiro de texto (ex: input.txt) com as duas configurações inicial e final no formato seguinte:

        1 2 3 4 5 6 8 12 13 9 0 7 14 11 10 15
        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0

    onde a primeira linha representa o problema e a segunda representa o objetivo (goal).

    Assim, para, por exemplo, testar BFS para as configurações a cima é preciso:

        -Criar um ficheiro de texto "input.txt" usando o comando "cat > input.txt" no terminal e escrever as configurações desejadas no formato já indicado;
        -No terminal, escrever "python3 BFS.py < input.txt" (sem aspas), onde python3 é a forma de invocar o código, BFS é o algoritmo escolhido (não esquecer a extenção .py que faz parte da invocação) e input.txt é o ficheiro de texto que vai ser redirecionado para o ficheiro BFS.py como input através do símbolo "<".

        Nota: todos os ficheiros da pasta são necessários para uma boa execução.


    Para analizar o código:

        Cada ficheiro corresponde a cada algoritmo de pesquisa, possuindo todas as funções necessárias para a busca, excepto para os algoritmos BFS e DFS cujo algoritmo base semelhante a ambos se une num só ficheiro: simpleuninformed.py .

        Para além de ficheiros que contêm os algoritmos, existem também:
            
            - "Board.py" onde se encontra o código com a class Board onde está definido e representado o jogo, as suas regras e os seus movimentos.
            - "Node" onde se encontra a class Node que represnta os nós usados para pesquisa não informada e informada apenas com heurísitca "manhattan".
            - "NodeMis" onde se encontra a class NodeMis que representa os nós usados para pesquisa informada apenas com heurística "misplaced".


    