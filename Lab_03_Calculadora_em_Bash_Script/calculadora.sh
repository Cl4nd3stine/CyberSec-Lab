#!/bin/bash
while true; do
        clear;
        echo "1 - Soma"
        echo "2 - Subtração"
        echo "3 - Multiplicação"
        echo "4 - Divisão"
        echo "5 - Sair"
        echo ""
        echo "Digite uma opção"
        read opcao

        if [ "$opcao" -eq 5 ] ; then
              exit
        fi

        echo "Digite o primeiro número:"
        read num1;
        echo "Digite o segundo número:"
        read num2;

        case $opcao in
             1)
               resultado=`expr $num1 + $num2`;
               echo "O resultado é: $resultado";;
             2)
               resultado=`expr $num1 - $num2`;
               echo "O resultado é: $resultado";;
             3)
               resultado=`expr $num1 \* $num2`;
               echo "O resultado é: $resultado";;
             4)
               if [ $num2 -eq 0 ]; then
                  echo "Erro: Divisão por zero não permitida."
               else
                  resultado=`expr $num1 / $num2`;
                  echo "O resultado é: $resultado";
               fi;;
             *)
               echo "Digite uma opção válida";;
        esac
        sleep 5;
done