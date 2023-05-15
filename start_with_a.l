%{
/* Lex Program to accept string starting with vowel */
%}
A [A][a-z A-Z]+
a [a][a-z A-Z]+
b [^A][a-z A-Z]+
c [^a][a-z A-z]+
%%
{A} printf("Accepted");
{a} printf("Accepted");
{b} printf("Not accepted");
{c} printf("Not accepted");
%%
main()
{
yylex();
}
int yywrap(){
return 1;
}