%{
 /*program*/
%}
Oct[o][0-7]+
Hex[0][x][X][0-9 A-F]+
%%
{Hex} printf("This is Hexadecimal number");
{Oct} printf("This is an Octal number");
%%
main()
{
yylex();
}
int yywrap()
{
return 1;
}