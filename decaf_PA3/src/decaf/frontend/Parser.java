//### This file created by BYACC 1.8(/Java extension  1.13)
//### Java capabilities added 7 Jan 97, Bob Jamison
//### Updated : 27 Nov 97  -- Bob Jamison, Joe Nieten
//###           01 Jan 98  -- Bob Jamison -- fixed generic semantic constructor
//###           01 Jun 99  -- Bob Jamison -- added Runnable support
//###           06 Aug 00  -- Bob Jamison -- made state variables class-global
//###           03 Jan 01  -- Bob Jamison -- improved flags, tracing
//###           16 May 01  -- Bob Jamison -- added custom stack sizing
//###           04 Mar 02  -- Yuval Oren  -- improved java performance, added options
//###           14 Mar 02  -- Tomas Hurka -- -d support, static initializer workaround
//###           14 Sep 06  -- Keltin Leung-- ReduceListener support, eliminate underflow report in error recovery
//### Please send bug reports to tom@hukatronic.cz
//### static char yysccsid[] = "@(#)yaccpar	1.8 (Berkeley) 01/20/90";






//#line 11 "Parser.y"
package decaf.frontend;

import decaf.tree.Tree;
import decaf.tree.Tree.*;
import decaf.error.*;
import java.util.*;
//#line 25 "Parser.java"
interface ReduceListener {
  public boolean onReduce(String rule);
}




public class Parser
             extends BaseParser
             implements ReduceListener
{

boolean yydebug;        //do I want debug output?
int yynerrs;            //number of errors so far
int yyerrflag;          //was there an error?
int yychar;             //the current working character

ReduceListener reduceListener = null;
void yyclearin ()       {yychar = (-1);}
void yyerrok ()         {yyerrflag=0;}
void addReduceListener(ReduceListener l) {
  reduceListener = l;}


//########## MESSAGES ##########
//###############################################################
// method: debug
//###############################################################
void debug(String msg)
{
  if (yydebug)
    System.out.println(msg);
}

//########## STATE STACK ##########
final static int YYSTACKSIZE = 500;  //maximum stack size
int statestk[] = new int[YYSTACKSIZE]; //state stack
int stateptr;
int stateptrmax;                     //highest index of stackptr
int statemax;                        //state when highest index reached
//###############################################################
// methods: state stack push,pop,drop,peek
//###############################################################
final void state_push(int state)
{
  try {
		stateptr++;
		statestk[stateptr]=state;
	 }
	 catch (ArrayIndexOutOfBoundsException e) {
     int oldsize = statestk.length;
     int newsize = oldsize * 2;
     int[] newstack = new int[newsize];
     System.arraycopy(statestk,0,newstack,0,oldsize);
     statestk = newstack;
     statestk[stateptr]=state;
  }
}
final int state_pop()
{
  return statestk[stateptr--];
}
final void state_drop(int cnt)
{
  stateptr -= cnt; 
}
final int state_peek(int relative)
{
  return statestk[stateptr-relative];
}
//###############################################################
// method: init_stacks : allocate and prepare stacks
//###############################################################
final boolean init_stacks()
{
  stateptr = -1;
  val_init();
  return true;
}
//###############################################################
// method: dump_stacks : show n levels of the stacks
//###############################################################
void dump_stacks(int count)
{
int i;
  System.out.println("=index==state====value=     s:"+stateptr+"  v:"+valptr);
  for (i=0;i<count;i++)
    System.out.println(" "+i+"    "+statestk[i]+"      "+valstk[i]);
  System.out.println("======================");
}


//########## SEMANTIC VALUES ##########
//## **user defined:SemValue
String   yytext;//user variable to return contextual strings
SemValue yyval; //used to return semantic vals from action routines
SemValue yylval;//the 'lval' (result) I got from yylex()
SemValue valstk[] = new SemValue[YYSTACKSIZE];
int valptr;
//###############################################################
// methods: value stack push,pop,drop,peek.
//###############################################################
final void val_init()
{
  yyval=new SemValue();
  yylval=new SemValue();
  valptr=-1;
}
final void val_push(SemValue val)
{
  try {
    valptr++;
    valstk[valptr]=val;
  }
  catch (ArrayIndexOutOfBoundsException e) {
    int oldsize = valstk.length;
    int newsize = oldsize*2;
    SemValue[] newstack = new SemValue[newsize];
    System.arraycopy(valstk,0,newstack,0,oldsize);
    valstk = newstack;
    valstk[valptr]=val;
  }
}
final SemValue val_pop()
{
  return valstk[valptr--];
}
final void val_drop(int cnt)
{
  valptr -= cnt;
}
final SemValue val_peek(int relative)
{
  return valstk[valptr-relative];
}
//#### end semantic value section ####
public final static short VOID=257;
public final static short BOOL=258;
public final static short INT=259;
public final static short STRING=260;
public final static short CLASS=261;
public final static short NULL=262;
public final static short EXTENDS=263;
public final static short THIS=264;
public final static short WHILE=265;
public final static short FOR=266;
public final static short IF=267;
public final static short ELSE=268;
public final static short RETURN=269;
public final static short BREAK=270;
public final static short NEW=271;
public final static short PRINT=272;
public final static short READ_INTEGER=273;
public final static short READ_LINE=274;
public final static short LITERAL=275;
public final static short IDENTIFIER=276;
public final static short AND=277;
public final static short OR=278;
public final static short STATIC=279;
public final static short INSTANCEOF=280;
public final static short LESS_EQUAL=281;
public final static short GREATER_EQUAL=282;
public final static short EQUAL=283;
public final static short NOT_EQUAL=284;
public final static short INC=285;
public final static short DEC=286;
public final static short NUMINSTANCES=287;
public final static short FI=288;
public final static short DO=289;
public final static short OD=290;
public final static short GUARD=291;
public final static short UMINUS=292;
public final static short EMPTY=293;
public final static short YYERRCODE=256;
final static short yylhs[] = {                           -1,
    0,    1,    1,    3,    4,    5,    5,    5,    5,    5,
    5,    2,    6,    6,    7,    7,    7,    9,    9,   10,
   10,    8,    8,   11,   12,   12,   13,   13,   13,   13,
   13,   13,   13,   13,   13,   13,   13,   14,   14,   14,
   26,   26,   23,   23,   25,   24,   24,   24,   24,   24,
   24,   24,   24,   24,   24,   24,   24,   24,   24,   24,
   24,   24,   24,   24,   24,   24,   24,   24,   24,   24,
   24,   24,   24,   24,   24,   24,   24,   28,   28,   27,
   27,   29,   29,   16,   17,   20,   15,   30,   30,   18,
   18,   19,   21,   22,   31,   31,   32,
};
final static short yylen[] = {                            2,
    1,    2,    1,    2,    2,    1,    1,    1,    1,    2,
    3,    6,    2,    0,    2,    2,    0,    1,    0,    3,
    1,    7,    6,    3,    2,    0,    1,    2,    1,    1,
    1,    2,    2,    2,    1,    1,    1,    3,    1,    0,
    2,    0,    2,    4,    5,    2,    2,    2,    2,    1,
    1,    1,    3,    3,    3,    3,    3,    3,    3,    3,
    3,    3,    3,    3,    3,    3,    2,    2,    5,    3,
    3,    1,    4,    5,    6,    4,    5,    1,    1,    1,
    0,    3,    1,    5,    9,    1,    6,    2,    0,    2,
    1,    4,    3,    3,    3,    1,    3,
};
final static short yydefred[] = {                         0,
    0,    0,    0,    3,    0,    2,    0,    0,   13,   17,
    0,    7,    8,    6,    9,    0,    0,   12,   15,    0,
    0,   16,   10,    0,    4,    0,    0,    0,    0,   11,
    0,   21,    0,    0,    0,    0,    5,    0,    0,    0,
   26,   23,   20,   22,    0,   79,   72,    0,    0,    0,
    0,   86,    0,    0,    0,    0,   78,    0,    0,    0,
    0,    0,    0,    0,    0,   24,   27,   37,   25,    0,
   29,   30,   31,    0,    0,    0,   35,   36,    0,    0,
    0,    0,   52,    0,    0,    0,    0,    0,   51,    0,
   96,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,   28,   32,   33,   34,
   48,   49,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,   41,    0,    0,    0,
    0,    0,    0,    0,   93,    0,    0,    0,    0,    0,
   70,   71,    0,    0,   94,    0,   66,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,   97,   95,   73,
    0,    0,   92,    0,   76,    0,   44,    0,    0,    0,
   84,    0,    0,   74,    0,    0,   77,    0,   45,    0,
    0,   87,   75,    0,   88,    0,   85,
};
final static short yydgoto[] = {                          2,
    3,    4,   67,   20,   33,    8,   11,   22,   34,   35,
   68,   45,   69,   70,   71,   72,   73,   74,   75,   76,
   77,   78,   87,   80,   89,   82,  179,   83,  140,  192,
   90,   91,
};
final static short yysindex[] = {                      -236,
 -242,    0, -236,    0, -220,    0, -224,  -63,    0,    0,
  -75,    0,    0,    0,    0, -209, -115,    0,    0,   13,
  -83,    0,    0,  -74,    0,   37,  -11,   51, -115,    0,
 -115,    0,  -73,   64,   54,   69,    0,  -17, -115,  -17,
    0,    0,    0,    0,    2,    0,    0,   71,   72,  115,
  123,    0, -238,   74,   75,   76,    0,   77,  123,  123,
   79,  123,  123,  123,   88,    0,    0,    0,    0,   61,
    0,    0,    0,   63,   67,   73,    0,    0,   -5,  952,
    0, -152,    0,  123,  123,   88, -253,  649,    0, -285,
    0,  952,   90,   40,  123,   93,   97,  123, -253, -253,
 -139, -188,  -37,  -37, -137,  692,    0,    0,    0,    0,
    0,    0,  123,  123,  123,  123,  123,  123,  123,  123,
  123,  123,  123,  123,  123,  123,    0,  123,  123,  100,
  792,   91,  819,   35,    0,  123,  106,   96,  952,    5,
    0,    0,  843,  111,    0,  112,    0,  952, 1102, 1003,
   -6,   -6,  -32,  -32,   16,   16,  -37,  -37,  -37,   -6,
   -6,  854,  919,  123,   35,  123,   68,    0,    0,    0,
  941,  123,    0, -122,    0,  123,    0,  123,  116,  117,
    0,  876, -109,    0,  952,  121,    0,  952,    0,  123,
   35,    0,    0,  124,    0,   35,    0,
};
final static short yyrindex[] = {                         0,
    0,    0,  164,    0,   44,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,  107,    0,    0,  128,    0,
  128,    0,    0,    0,  130,    0,    0,    0,    0,    0,
    0,    0,    0,    0,  -58,    0,    0,    0,    0, -104,
  -57,    0,    0,    0,    0,    0,    0,    0, -104, -104,
    0, -104, -104, -104, -104,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,  976,    0,
  594,    0,    0, -104,  -58, -104,  382,    0,    0,    0,
    0,  118,    0,    0, -104,    0,    0, -104,  406,  442,
    0,    0,  466,  495,    0,    0,    0,    0,    0,    0,
    0,    0, -104, -104, -104, -104, -104, -104, -104, -104,
 -104, -104, -104, -104, -104, -104,    0, -104, -104,  153,
    0,    0,    0,  -58,    0, -104,    0, -104,   32,    0,
    0,    0,    0,    0,    0,    0,    0,  -14,    7,   20,
  129,  967,  673,  900, 1047, 1122,  504,  531,  540, 1020,
 1111,    0,    0,  -25,  -58, -104,  567,    0,    0,    0,
    0, -104,    0,    0,    0, -104,    0, -104,    0,  135,
    0,    0,  -33,    0,   43,    0,    0,   30,    0,    3,
  -58,    0,    0,    0,    0,  -58,    0,
};
final static short yygindex[] = {                         0,
    0,  175,  168,   65,   82,    0,    0,    0,  150,    0,
   57,    0, -110,  -81,    0,    0,    0,    0,    0,    0,
    0,    0, 1127, 1295,  -16,    0,    0,    0,   41,    0,
  139,   70,
};
final static int YYTABLESIZE=1473;
static short yytable[];
static { yytable();}
static void yytable(){
yytable = new short[]{                         89,
   40,   91,  135,  132,  124,  136,   89,   27,  127,  122,
  120,   89,  121,  127,  123,   81,   27,   27,   12,   13,
   14,   15,   16,  168,    1,   89,   38,  126,   81,  125,
  124,  111,  112,    5,   64,  122,  120,   93,  121,  127,
  123,   65,    7,   40,   38,  173,   63,   64,  172,   18,
   64,    9,  124,  128,  181,  113,  183,  122,  128,   10,
   65,  127,  123,   65,   64,   64,   23,   64,   81,   64,
   69,   25,   83,   69,   65,   83,   29,   65,   65,   63,
  195,   30,   65,   82,  128,  197,   82,   69,   69,   89,
   31,   89,   21,   32,   42,   32,   44,   39,   24,   64,
   64,  145,  136,   43,   38,   41,  128,   65,  194,   40,
   84,   85,   65,   95,   96,   97,   98,   81,  101,  107,
   64,  108,   69,  130,   41,  109,   66,   65,   64,  137,
  138,  110,   63,  141,   94,   65,  144,  142,  146,  164,
   63,   12,   13,   14,   15,   16,  170,   64,   81,  166,
   81,  175,  176,  186,   86,   64,  189,   41,  191,   63,
  172,  193,   65,    1,  196,    5,   14,   63,   19,   62,
   18,   42,   62,   81,   81,   80,   90,    6,   19,   81,
   36,   12,   13,   14,   15,   16,   62,   62,   30,   43,
   41,   62,   26,   43,   43,   43,   43,   43,   43,   43,
  102,   28,   37,   17,  180,  169,    0,    0,    0,    0,
   43,   43,   43,   43,   43,   43,    0,   42,   42,    0,
    0,   62,    0,   89,   89,   89,   89,   89,   89,    0,
   89,   89,   89,   89,    0,   89,   89,   89,   89,   89,
   89,   89,   89,   43,    0,   43,   89,    0,  116,  117,
   42,   89,   89,   89,   89,   89,   89,   89,   12,   13,
   14,   15,   16,   46,    0,   47,   48,   49,   50,    0,
   51,   52,   53,   54,   55,   56,   57,    0,   42,  111,
  112,   58,    0,   64,   64,    0,   59,   60,   61,    0,
   62,   12,   13,   14,   15,   16,   46,   65,   47,   48,
   49,   50,    0,   51,   52,   53,   54,   55,   56,   57,
    0,    0,    0,    0,   58,    0,    0,    0,    0,   59,
   60,   61,    0,   62,   12,   13,   14,   15,   16,   46,
    0,   47,   48,   49,   50,    0,   51,   52,   53,   54,
   55,   56,   57,    0,    0,    0,    0,   58,  105,   46,
    0,   47,   59,   60,   61,    0,   62,   46,   53,   47,
   55,   56,   57,    0,    0,    0,   53,   58,   55,   56,
   57,    0,   59,   60,   61,   58,   46,    0,   47,    0,
   59,   60,   61,    0,   46,   53,   47,   55,   56,   57,
    0,    0,    0,   53,   58,   55,   56,   57,    0,   59,
   60,   61,   58,    0,    0,   62,   62,   59,   60,   61,
    0,   62,   62,    0,    0,    0,    0,    0,   50,    0,
    0,    0,   50,   50,   50,   50,   50,   50,   50,   43,
   43,    0,    0,   43,   43,   43,   43,   43,   43,   50,
   50,   50,   46,   50,   50,    0,   46,   46,   46,   46,
   46,   46,   46,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,   46,   46,   46,    0,   46,   46,    0,
    0,    0,   50,    0,   50,    0,    0,    0,   47,    0,
    0,    0,   47,   47,   47,   47,   47,   47,   47,    0,
    0,    0,    0,    0,    0,    0,   46,    0,   46,   47,
   47,   47,   67,   47,   47,    0,   67,   67,   67,   67,
   67,    0,   67,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,   67,   67,   67,    0,   67,   67,    0,
    0,   68,   47,    0,   47,   68,   68,   68,   68,   68,
   55,   68,    0,    0,   55,   55,   55,   55,   55,    0,
   55,    0,   68,   68,   68,    0,   68,   68,   67,    0,
    0,   55,   55,   55,    0,   55,   55,   56,    0,    0,
    0,   56,   56,   56,   56,   56,   57,   56,    0,    0,
   57,   57,   57,   57,   57,    0,   57,   68,   56,   56,
   56,    0,   56,   56,    0,    0,   55,   57,   57,   57,
    0,   57,   57,   66,    0,    0,    0,    0,   66,   66,
    0,   66,   66,   66,    0,    0,    0,    0,    0,    0,
    0,    0,    0,   56,   66,   40,   66,    0,   66,   66,
   51,    0,   57,    0,   39,   51,   51,    0,   51,   51,
   51,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,   39,   51,    0,   51,   51,   66,   50,   50,
    0,    0,   50,   50,   50,   50,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,   46,   46,   51,  124,   46,   46,   46,   46,
  122,  120,    0,  121,  127,  123,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,  134,    0,  126,    0,
  125,  129,    0,   58,    0,    0,   58,    0,   47,   47,
    0,    0,   47,   47,   47,   47,    0,    0,  124,    0,
   58,   58,  147,  122,  120,   58,  121,  127,  123,  128,
    0,    0,   67,   67,    0,    0,   67,   67,   67,   67,
    0,  126,    0,  125,  129,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,   58,    0,    0,    0,    0,
    0,   68,   68,    0,    0,   68,   68,   68,   68,    0,
   55,   55,  128,    0,   55,   55,   55,   55,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,   56,   56,    0,
    0,   56,   56,   56,   56,    0,   57,   57,    0,    0,
   57,   57,   57,   57,    0,    0,    0,    0,  124,    0,
    0,    0,  165,  122,  120,    0,  121,  127,  123,    0,
    0,    0,   42,   66,   66,    0,    0,   66,   66,   66,
   66,  126,    0,  125,  129,  124,    0,    0,    0,  167,
  122,  120,    0,  121,  127,  123,    0,    0,    0,    0,
   51,   51,    0,    0,   51,   51,   51,   51,  126,  124,
  125,  129,  128,    0,  122,  120,  174,  121,  127,  123,
  124,    0,    0,    0,    0,  122,  120,    0,  121,  127,
  123,    0,  126,    0,  125,  129,    0,    0,    0,  128,
    0,    0,  124,  126,    0,  125,  129,  122,  120,    0,
  121,  127,  123,    0,    0,  114,  115,    0,    0,  116,
  117,  118,  119,  128,  190,  126,    0,  125,  129,    0,
   59,    0,    0,   59,  128,    0,  177,    0,    0,   58,
   58,    0,    0,    0,    0,  124,    0,   59,   59,    0,
  122,  120,   59,  121,  127,  123,  128,    0,  114,  115,
    0,    0,  116,  117,  118,  119,  178,  124,  126,    0,
  125,  129,  122,  120,    0,  121,  127,  123,  124,    0,
    0,    0,   59,  122,  120,    0,  121,  127,  123,    0,
  126,    0,  125,  129,    0,    0,    0,   63,    0,  128,
   63,  126,   50,  125,  129,    0,    0,   50,   50,    0,
   50,   50,   50,    0,   63,   63,    0,    0,    0,   63,
    0,  128,    0,  184,    0,   50,    0,   50,   50,  124,
    0,    0,  128,    0,  122,  120,    0,  121,  127,  123,
    0,    0,    0,    0,    0,    0,    0,    0,    0,   63,
   61,    0,  126,   61,  125,    0,   50,    0,  114,  115,
    0,    0,  116,  117,  118,  119,    0,   61,   61,    0,
    0,    0,   61,    0,    0,    0,    0,   53,    0,   53,
   53,   53,    0,  128,    0,  114,  115,    0,    0,  116,
  117,  118,  119,    0,   53,   53,   53,    0,   53,   53,
    0,    0,   61,    0,    0,    0,    0,    0,    0,  114,
  115,    0,    0,  116,  117,  118,  119,    0,    0,    0,
  114,  115,    0,    0,  116,  117,  118,  119,  124,   53,
    0,    0,    0,  122,  120,    0,  121,  127,  123,    0,
    0,   60,  114,  115,   60,    0,  116,  117,  118,  119,
    0,  126,   54,  125,   54,   54,   54,    0,   60,   60,
    0,   79,    0,   60,    0,    0,   59,   59,    0,   54,
   54,   54,    0,   54,   54,   99,  100,    0,    0,    0,
    0,    0,  128,    0,    0,  114,  115,    0,    0,  116,
  117,  118,  119,   60,    0,    0,    0,    0,    0,    0,
    0,   79,    0,    0,   54,    0,    0,  114,  115,    0,
    0,  116,  117,  118,  119,    0,    0,    0,  114,  115,
    0,    0,  116,  117,  118,  119,    0,    0,    0,    0,
    0,    0,    0,   63,   63,    0,    0,    0,    0,   63,
   63,    0,   50,   50,    0,    0,   50,   50,   50,   50,
   79,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,  114,
    0,    0,    0,  116,  117,  118,  119,    0,    0,    0,
    0,   79,    0,   79,    0,    0,   61,   61,    0,    0,
    0,    0,   61,   61,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,   79,   79,    0,    0,
    0,    0,   79,   53,   53,    0,    0,   53,   53,   53,
   53,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,   88,   92,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,   88,  103,  104,  106,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,  131,    0,
  133,    0,  116,  117,  118,  119,    0,   60,   60,  139,
    0,    0,  143,   60,   60,    0,    0,    0,   54,   54,
    0,    0,   54,   54,   54,   54,    0,  148,  149,  150,
  151,  152,  153,  154,  155,  156,  157,  158,  159,  160,
  161,    0,  162,  163,    0,    0,    0,    0,    0,    0,
   88,    0,  171,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,  139,    0,
  182,    0,    0,    0,    0,    0,  185,    0,    0,    0,
  187,    0,  188,
};
}
static short yycheck[];
static { yycheck(); }
static void yycheck() {
yycheck = new short[] {                         33,
   59,   59,  288,   85,   37,  291,   40,   91,   46,   42,
   43,   45,   45,   46,   47,   41,   91,   91,  257,  258,
  259,  260,  261,  134,  261,   59,   41,   60,   45,   62,
   37,  285,  286,  276,   33,   42,   43,  276,   45,   46,
   47,   40,  263,   41,   59,   41,   45,   41,   44,  125,
   44,  276,   37,   91,  165,   61,  167,   42,   91,  123,
   41,   46,   47,   44,   58,   59,  276,   33,   85,   63,
   41,   59,   41,   44,   40,   44,   40,   58,   59,   45,
  191,   93,   63,   41,   91,  196,   44,   58,   59,  123,
   40,  125,   11,   29,   38,   31,   40,   44,   17,   93,
   33,  290,  291,   39,   41,  123,   91,   40,  190,   41,
   40,   40,   93,   40,   40,   40,   40,  134,   40,   59,
   33,   59,   93,  276,  123,   59,  125,   40,   33,   40,
   91,   59,   45,   41,   53,   40,  276,   41,  276,   40,
   45,  257,  258,  259,  260,  261,   41,   33,  165,   59,
  167,   41,   41,  276,   40,   33,   41,  123,  268,   45,
   44,   41,   40,    0,   41,   59,  123,   45,   41,   41,
   41,  276,   44,  190,  191,   41,   59,    3,   11,  196,
   31,  257,  258,  259,  260,  261,   58,   59,   93,   37,
  123,   63,  276,   41,   42,   43,   44,   45,   46,   47,
   62,  276,  276,  279,  164,  136,   -1,   -1,   -1,   -1,
   58,   59,   60,   61,   62,   63,   -1,  276,  276,   -1,
   -1,   93,   -1,  257,  258,  259,  260,  261,  262,   -1,
  264,  265,  266,  267,   -1,  269,  270,  271,  272,  273,
  274,  275,  276,   91,   -1,   93,  280,   -1,  281,  282,
  276,  285,  286,  287,  288,  289,  290,  291,  257,  258,
  259,  260,  261,  262,   -1,  264,  265,  266,  267,   -1,
  269,  270,  271,  272,  273,  274,  275,   -1,  276,  285,
  286,  280,   -1,  277,  278,   -1,  285,  286,  287,   -1,
  289,  257,  258,  259,  260,  261,  262,  278,  264,  265,
  266,  267,   -1,  269,  270,  271,  272,  273,  274,  275,
   -1,   -1,   -1,   -1,  280,   -1,   -1,   -1,   -1,  285,
  286,  287,   -1,  289,  257,  258,  259,  260,  261,  262,
   -1,  264,  265,  266,  267,   -1,  269,  270,  271,  272,
  273,  274,  275,   -1,   -1,   -1,   -1,  280,  261,  262,
   -1,  264,  285,  286,  287,   -1,  289,  262,  271,  264,
  273,  274,  275,   -1,   -1,   -1,  271,  280,  273,  274,
  275,   -1,  285,  286,  287,  280,  262,   -1,  264,   -1,
  285,  286,  287,   -1,  262,  271,  264,  273,  274,  275,
   -1,   -1,   -1,  271,  280,  273,  274,  275,   -1,  285,
  286,  287,  280,   -1,   -1,  277,  278,  285,  286,  287,
   -1,  283,  284,   -1,   -1,   -1,   -1,   -1,   37,   -1,
   -1,   -1,   41,   42,   43,   44,   45,   46,   47,  277,
  278,   -1,   -1,  281,  282,  283,  284,  285,  286,   58,
   59,   60,   37,   62,   63,   -1,   41,   42,   43,   44,
   45,   46,   47,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   58,   59,   60,   -1,   62,   63,   -1,
   -1,   -1,   91,   -1,   93,   -1,   -1,   -1,   37,   -1,
   -1,   -1,   41,   42,   43,   44,   45,   46,   47,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   91,   -1,   93,   58,
   59,   60,   37,   62,   63,   -1,   41,   42,   43,   44,
   45,   -1,   47,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   58,   59,   60,   -1,   62,   63,   -1,
   -1,   37,   91,   -1,   93,   41,   42,   43,   44,   45,
   37,   47,   -1,   -1,   41,   42,   43,   44,   45,   -1,
   47,   -1,   58,   59,   60,   -1,   62,   63,   93,   -1,
   -1,   58,   59,   60,   -1,   62,   63,   37,   -1,   -1,
   -1,   41,   42,   43,   44,   45,   37,   47,   -1,   -1,
   41,   42,   43,   44,   45,   -1,   47,   93,   58,   59,
   60,   -1,   62,   63,   -1,   -1,   93,   58,   59,   60,
   -1,   62,   63,   37,   -1,   -1,   -1,   -1,   42,   43,
   -1,   45,   46,   47,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   93,   58,   59,   60,   -1,   62,   63,
   37,   -1,   93,   -1,   41,   42,   43,   -1,   45,   46,
   47,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   59,   60,   -1,   62,   63,   91,  277,  278,
   -1,   -1,  281,  282,  283,  284,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,  277,  278,   91,   37,  281,  282,  283,  284,
   42,   43,   -1,   45,   46,   47,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   58,   -1,   60,   -1,
   62,   63,   -1,   41,   -1,   -1,   44,   -1,  277,  278,
   -1,   -1,  281,  282,  283,  284,   -1,   -1,   37,   -1,
   58,   59,   41,   42,   43,   63,   45,   46,   47,   91,
   -1,   -1,  277,  278,   -1,   -1,  281,  282,  283,  284,
   -1,   60,   -1,   62,   63,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   93,   -1,   -1,   -1,   -1,
   -1,  277,  278,   -1,   -1,  281,  282,  283,  284,   -1,
  277,  278,   91,   -1,  281,  282,  283,  284,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,  277,  278,   -1,
   -1,  281,  282,  283,  284,   -1,  277,  278,   -1,   -1,
  281,  282,  283,  284,   -1,   -1,   -1,   -1,   37,   -1,
   -1,   -1,   41,   42,   43,   -1,   45,   46,   47,   -1,
   -1,   -1,  276,  277,  278,   -1,   -1,  281,  282,  283,
  284,   60,   -1,   62,   63,   37,   -1,   -1,   -1,   41,
   42,   43,   -1,   45,   46,   47,   -1,   -1,   -1,   -1,
  277,  278,   -1,   -1,  281,  282,  283,  284,   60,   37,
   62,   63,   91,   -1,   42,   43,   44,   45,   46,   47,
   37,   -1,   -1,   -1,   -1,   42,   43,   -1,   45,   46,
   47,   -1,   60,   -1,   62,   63,   -1,   -1,   -1,   91,
   -1,   -1,   37,   60,   -1,   62,   63,   42,   43,   -1,
   45,   46,   47,   -1,   -1,  277,  278,   -1,   -1,  281,
  282,  283,  284,   91,   59,   60,   -1,   62,   63,   -1,
   41,   -1,   -1,   44,   91,   -1,   93,   -1,   -1,  277,
  278,   -1,   -1,   -1,   -1,   37,   -1,   58,   59,   -1,
   42,   43,   63,   45,   46,   47,   91,   -1,  277,  278,
   -1,   -1,  281,  282,  283,  284,   58,   37,   60,   -1,
   62,   63,   42,   43,   -1,   45,   46,   47,   37,   -1,
   -1,   -1,   93,   42,   43,   -1,   45,   46,   47,   -1,
   60,   -1,   62,   63,   -1,   -1,   -1,   41,   -1,   91,
   44,   60,   37,   62,   63,   -1,   -1,   42,   43,   -1,
   45,   46,   47,   -1,   58,   59,   -1,   -1,   -1,   63,
   -1,   91,   -1,   93,   -1,   60,   -1,   62,   63,   37,
   -1,   -1,   91,   -1,   42,   43,   -1,   45,   46,   47,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   93,
   41,   -1,   60,   44,   62,   -1,   91,   -1,  277,  278,
   -1,   -1,  281,  282,  283,  284,   -1,   58,   59,   -1,
   -1,   -1,   63,   -1,   -1,   -1,   -1,   41,   -1,   43,
   44,   45,   -1,   91,   -1,  277,  278,   -1,   -1,  281,
  282,  283,  284,   -1,   58,   59,   60,   -1,   62,   63,
   -1,   -1,   93,   -1,   -1,   -1,   -1,   -1,   -1,  277,
  278,   -1,   -1,  281,  282,  283,  284,   -1,   -1,   -1,
  277,  278,   -1,   -1,  281,  282,  283,  284,   37,   93,
   -1,   -1,   -1,   42,   43,   -1,   45,   46,   47,   -1,
   -1,   41,  277,  278,   44,   -1,  281,  282,  283,  284,
   -1,   60,   41,   62,   43,   44,   45,   -1,   58,   59,
   -1,   45,   -1,   63,   -1,   -1,  277,  278,   -1,   58,
   59,   60,   -1,   62,   63,   59,   60,   -1,   -1,   -1,
   -1,   -1,   91,   -1,   -1,  277,  278,   -1,   -1,  281,
  282,  283,  284,   93,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   85,   -1,   -1,   93,   -1,   -1,  277,  278,   -1,
   -1,  281,  282,  283,  284,   -1,   -1,   -1,  277,  278,
   -1,   -1,  281,  282,  283,  284,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,  277,  278,   -1,   -1,   -1,   -1,  283,
  284,   -1,  277,  278,   -1,   -1,  281,  282,  283,  284,
  134,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,  277,
   -1,   -1,   -1,  281,  282,  283,  284,   -1,   -1,   -1,
   -1,  165,   -1,  167,   -1,   -1,  277,  278,   -1,   -1,
   -1,   -1,  283,  284,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,  190,  191,   -1,   -1,
   -1,   -1,  196,  277,  278,   -1,   -1,  281,  282,  283,
  284,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   50,   51,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   62,   63,   64,   65,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   84,   -1,
   86,   -1,  281,  282,  283,  284,   -1,  277,  278,   95,
   -1,   -1,   98,  283,  284,   -1,   -1,   -1,  277,  278,
   -1,   -1,  281,  282,  283,  284,   -1,  113,  114,  115,
  116,  117,  118,  119,  120,  121,  122,  123,  124,  125,
  126,   -1,  128,  129,   -1,   -1,   -1,   -1,   -1,   -1,
  136,   -1,  138,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,  164,   -1,
  166,   -1,   -1,   -1,   -1,   -1,  172,   -1,   -1,   -1,
  176,   -1,  178,
};
}
final static short YYFINAL=2;
final static short YYMAXTOKEN=293;
final static String yyname[] = {
"end-of-file",null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,"'!'",null,null,null,"'%'",null,null,"'('","')'","'*'","'+'",
"','","'-'","'.'","'/'",null,null,null,null,null,null,null,null,null,null,"':'",
"';'","'<'","'='","'>'","'?'",null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,"'['",null,"']'",null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,"'{'",null,"'}'",null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,"VOID","BOOL","INT","STRING",
"CLASS","NULL","EXTENDS","THIS","WHILE","FOR","IF","ELSE","RETURN","BREAK",
"NEW","PRINT","READ_INTEGER","READ_LINE","LITERAL","IDENTIFIER","AND","OR",
"STATIC","INSTANCEOF","LESS_EQUAL","GREATER_EQUAL","EQUAL","NOT_EQUAL","INC",
"DEC","NUMINSTANCES","FI","DO","OD","GUARD","UMINUS","EMPTY",
};
final static String yyrule[] = {
"$accept : Program",
"Program : ClassList",
"ClassList : ClassList ClassDef",
"ClassList : ClassDef",
"VariableDef : Variable ';'",
"Variable : Type IDENTIFIER",
"Type : INT",
"Type : VOID",
"Type : BOOL",
"Type : STRING",
"Type : CLASS IDENTIFIER",
"Type : Type '[' ']'",
"ClassDef : CLASS IDENTIFIER ExtendsClause '{' FieldList '}'",
"ExtendsClause : EXTENDS IDENTIFIER",
"ExtendsClause :",
"FieldList : FieldList VariableDef",
"FieldList : FieldList FunctionDef",
"FieldList :",
"Formals : VariableList",
"Formals :",
"VariableList : VariableList ',' Variable",
"VariableList : Variable",
"FunctionDef : STATIC Type IDENTIFIER '(' Formals ')' StmtBlock",
"FunctionDef : Type IDENTIFIER '(' Formals ')' StmtBlock",
"StmtBlock : '{' StmtList '}'",
"StmtList : StmtList Stmt",
"StmtList :",
"Stmt : VariableDef",
"Stmt : SimpleStmt ';'",
"Stmt : IfStmt",
"Stmt : WhileStmt",
"Stmt : ForStmt",
"Stmt : ReturnStmt ';'",
"Stmt : PrintStmt ';'",
"Stmt : BreakStmt ';'",
"Stmt : GuardedIfStmt",
"Stmt : GuardedDoStmt",
"Stmt : StmtBlock",
"SimpleStmt : LValue '=' Expr",
"SimpleStmt : Call",
"SimpleStmt :",
"Receiver : Expr '.'",
"Receiver :",
"LValue : Receiver IDENTIFIER",
"LValue : Expr '[' Expr ']'",
"Call : Receiver IDENTIFIER '(' Actuals ')'",
"Expr : INC LValue",
"Expr : DEC LValue",
"Expr : LValue INC",
"Expr : LValue DEC",
"Expr : LValue",
"Expr : Call",
"Expr : Constant",
"Expr : Expr '+' Expr",
"Expr : Expr '-' Expr",
"Expr : Expr '*' Expr",
"Expr : Expr '/' Expr",
"Expr : Expr '%' Expr",
"Expr : Expr EQUAL Expr",
"Expr : Expr NOT_EQUAL Expr",
"Expr : Expr '<' Expr",
"Expr : Expr '>' Expr",
"Expr : Expr LESS_EQUAL Expr",
"Expr : Expr GREATER_EQUAL Expr",
"Expr : Expr AND Expr",
"Expr : Expr OR Expr",
"Expr : '(' Expr ')'",
"Expr : '-' Expr",
"Expr : '!' Expr",
"Expr : Expr '?' Expr ':' Expr",
"Expr : READ_INTEGER '(' ')'",
"Expr : READ_LINE '(' ')'",
"Expr : THIS",
"Expr : NEW IDENTIFIER '(' ')'",
"Expr : NEW Type '[' Expr ']'",
"Expr : INSTANCEOF '(' Expr ',' IDENTIFIER ')'",
"Expr : NUMINSTANCES '(' IDENTIFIER ')'",
"Expr : '(' CLASS IDENTIFIER ')' Expr",
"Constant : LITERAL",
"Constant : NULL",
"Actuals : ExprList",
"Actuals :",
"ExprList : ExprList ',' Expr",
"ExprList : Expr",
"WhileStmt : WHILE '(' Expr ')' Stmt",
"ForStmt : FOR '(' SimpleStmt ';' Expr ';' SimpleStmt ')' Stmt",
"BreakStmt : BREAK",
"IfStmt : IF '(' Expr ')' Stmt ElseClause",
"ElseClause : ELSE Stmt",
"ElseClause :",
"ReturnStmt : RETURN Expr",
"ReturnStmt : RETURN",
"PrintStmt : PRINT '(' ExprList ')'",
"GuardedIfStmt : IF GuardedStmtList FI",
"GuardedDoStmt : DO GuardedStmtList OD",
"GuardedStmtList : GuardedStmtList GUARD GuardedStmt",
"GuardedStmtList : GuardedStmt",
"GuardedStmt : Expr ':' Stmt",
};

//#line 481 "Parser.y"
    
	/**
	 * 打印当前归约所用的语法规则<br>
	 * 请勿修改。
	 */
    public boolean onReduce(String rule) {
		if (rule.startsWith("$$"))
			return false;
		else
			rule = rule.replaceAll(" \\$\\$\\d+", "");

   	    if (rule.endsWith(":"))
    	    System.out.println(rule + " <empty>");
   	    else
			System.out.println(rule);
		return false;
    }
    
    public void diagnose() {
		addReduceListener(this);
		yyparse();
	}
//#line 702 "Parser.java"
//###############################################################
// method: yylexdebug : check lexer state
//###############################################################
void yylexdebug(int state,int ch)
{
String s=null;
  if (ch < 0) ch=0;
  if (ch <= YYMAXTOKEN) //check index bounds
     s = yyname[ch];    //now get it
  if (s==null)
    s = "illegal-symbol";
  debug("state "+state+", reading "+ch+" ("+s+")");
}





//The following are now global, to aid in error reporting
int yyn;       //next next thing to do
int yym;       //
int yystate;   //current parsing state from state table
String yys;    //current token string


//###############################################################
// method: yyparse : parse input and execute indicated items
//###############################################################
int yyparse()
{
boolean doaction;
  init_stacks();
  yynerrs = 0;
  yyerrflag = 0;
  yychar = -1;          //impossible char forces a read
  yystate=0;            //initial state
  state_push(yystate);  //save it
  while (true) //until parsing is done, either correctly, or w/error
    {
    doaction=true;
    //if (yydebug) debug("loop"); 
    //#### NEXT ACTION (from reduction table)
    for (yyn=yydefred[yystate];yyn==0;yyn=yydefred[yystate])
      {
      //if (yydebug) debug("yyn:"+yyn+"  state:"+yystate+"  yychar:"+yychar);
      if (yychar < 0)      //we want a char?
        {
        yychar = yylex();  //get next token
        //if (yydebug) debug(" next yychar:"+yychar);
        //#### ERROR CHECK ####
        //if (yychar < 0)    //it it didn't work/error
        //  {
        //  yychar = 0;      //change it to default string (no -1!)
          //if (yydebug)
          //  yylexdebug(yystate,yychar);
        //  }
        }//yychar<0
      yyn = yysindex[yystate];  //get amount to shift by (shift index)
      if ((yyn != 0) && (yyn += yychar) >= 0 &&
          yyn <= YYTABLESIZE && yycheck[yyn] == yychar)
        {
        //if (yydebug)
          //debug("state "+yystate+", shifting to state "+yytable[yyn]);
        //#### NEXT STATE ####
        yystate = yytable[yyn];//we are in a new state
        state_push(yystate);   //save it
        val_push(yylval);      //push our lval as the input for next rule
        yychar = -1;           //since we have 'eaten' a token, say we need another
        if (yyerrflag > 0)     //have we recovered an error?
           --yyerrflag;        //give ourselves credit
        doaction=false;        //but don't process yet
        break;   //quit the yyn=0 loop
        }

    yyn = yyrindex[yystate];  //reduce
    if ((yyn !=0 ) && (yyn += yychar) >= 0 &&
            yyn <= YYTABLESIZE && yycheck[yyn] == yychar)
      {   //we reduced!
      //if (yydebug) debug("reduce");
      yyn = yytable[yyn];
      doaction=true; //get ready to execute
      break;         //drop down to actions
      }
    else //ERROR RECOVERY
      {
      if (yyerrflag==0)
        {
        yyerror("syntax error");
        yynerrs++;
        }
      if (yyerrflag < 3) //low error count?
        {
        yyerrflag = 3;
        while (true)   //do until break
          {
          if (stateptr<0 || valptr<0)   //check for under & overflow here
            {
            return 1;
            }
          yyn = yysindex[state_peek(0)];
          if ((yyn != 0) && (yyn += YYERRCODE) >= 0 &&
                    yyn <= YYTABLESIZE && yycheck[yyn] == YYERRCODE)
            {
            //if (yydebug)
              //debug("state "+state_peek(0)+", error recovery shifting to state "+yytable[yyn]+" ");
            yystate = yytable[yyn];
            state_push(yystate);
            val_push(yylval);
            doaction=false;
            break;
            }
          else
            {
            //if (yydebug)
              //debug("error recovery discarding state "+state_peek(0)+" ");
            if (stateptr<0 || valptr<0)   //check for under & overflow here
              {
              return 1;
              }
            state_pop();
            val_pop();
            }
          }
        }
      else            //discard this token
        {
        if (yychar == 0)
          return 1; //yyabort
        //if (yydebug)
          //{
          //yys = null;
          //if (yychar <= YYMAXTOKEN) yys = yyname[yychar];
          //if (yys == null) yys = "illegal-symbol";
          //debug("state "+yystate+", error recovery discards token "+yychar+" ("+yys+")");
          //}
        yychar = -1;  //read another
        }
      }//end error recovery
    }//yyn=0 loop
    if (!doaction)   //any reason not to proceed?
      continue;      //skip action
    yym = yylen[yyn];          //get count of terminals on rhs
    //if (yydebug)
      //debug("state "+yystate+", reducing "+yym+" by rule "+yyn+" ("+yyrule[yyn]+")");
    if (yym>0)                 //if count of rhs not 'nil'
      yyval = val_peek(yym-1); //get current semantic value
    if (reduceListener == null || reduceListener.onReduce(yyrule[yyn])) // if intercepted!
      switch(yyn)
      {
//########## USER-SUPPLIED ACTIONS ##########
case 1:
//#line 55 "Parser.y"
{
						tree = new Tree.TopLevel(val_peek(0).clist, val_peek(0).loc);
					}
break;
case 2:
//#line 61 "Parser.y"
{
						yyval.clist.add(val_peek(0).cdef);
					}
break;
case 3:
//#line 65 "Parser.y"
{
                		yyval.clist = new ArrayList<Tree.ClassDef>();
                		yyval.clist.add(val_peek(0).cdef);
                	}
break;
case 5:
//#line 75 "Parser.y"
{
						yyval.vdef = new Tree.VarDef(val_peek(0).ident, val_peek(1).type, val_peek(0).loc);
					}
break;
case 6:
//#line 81 "Parser.y"
{
						yyval.type = new Tree.TypeIdent(Tree.INT, val_peek(0).loc);
					}
break;
case 7:
//#line 85 "Parser.y"
{
                		yyval.type = new Tree.TypeIdent(Tree.VOID, val_peek(0).loc);
                	}
break;
case 8:
//#line 89 "Parser.y"
{
                		yyval.type = new Tree.TypeIdent(Tree.BOOL, val_peek(0).loc);
                	}
break;
case 9:
//#line 93 "Parser.y"
{
                		yyval.type = new Tree.TypeIdent(Tree.STRING, val_peek(0).loc);
                	}
break;
case 10:
//#line 97 "Parser.y"
{
                		yyval.type = new Tree.TypeClass(val_peek(0).ident, val_peek(1).loc);
                	}
break;
case 11:
//#line 101 "Parser.y"
{
                		yyval.type = new Tree.TypeArray(val_peek(2).type, val_peek(2).loc);
                	}
break;
case 12:
//#line 107 "Parser.y"
{
						yyval.cdef = new Tree.ClassDef(val_peek(4).ident, val_peek(3).ident, val_peek(1).flist, val_peek(5).loc);
					}
break;
case 13:
//#line 113 "Parser.y"
{
						yyval.ident = val_peek(0).ident;
					}
break;
case 14:
//#line 117 "Parser.y"
{
                		yyval = new SemValue();
                	}
break;
case 15:
//#line 123 "Parser.y"
{
						yyval.flist.add(val_peek(0).vdef);
					}
break;
case 16:
//#line 127 "Parser.y"
{
						yyval.flist.add(val_peek(0).fdef);
					}
break;
case 17:
//#line 131 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.flist = new ArrayList<Tree>();
                	}
break;
case 19:
//#line 139 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.vlist = new ArrayList<Tree.VarDef>(); 
                	}
break;
case 20:
//#line 146 "Parser.y"
{
						yyval.vlist.add(val_peek(0).vdef);
					}
break;
case 21:
//#line 150 "Parser.y"
{
                		yyval.vlist = new ArrayList<Tree.VarDef>();
						yyval.vlist.add(val_peek(0).vdef);
                	}
break;
case 22:
//#line 157 "Parser.y"
{
						yyval.fdef = new MethodDef(true, val_peek(4).ident, val_peek(5).type, val_peek(2).vlist, (Block) val_peek(0).stmt, val_peek(4).loc);
					}
break;
case 23:
//#line 161 "Parser.y"
{
						yyval.fdef = new MethodDef(false, val_peek(4).ident, val_peek(5).type, val_peek(2).vlist, (Block) val_peek(0).stmt, val_peek(4).loc);
					}
break;
case 24:
//#line 167 "Parser.y"
{
						yyval.stmt = new Block(val_peek(1).slist, val_peek(2).loc);
					}
break;
case 25:
//#line 173 "Parser.y"
{
						yyval.slist.add(val_peek(0).stmt);
					}
break;
case 26:
//#line 177 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.slist = new ArrayList<Tree>();
                	}
break;
case 27:
//#line 184 "Parser.y"
{
						yyval.stmt = val_peek(0).vdef;
					}
break;
case 28:
//#line 189 "Parser.y"
{
                		if (yyval.stmt == null) {
                			yyval.stmt = new Tree.Skip(val_peek(0).loc);
                		}
                	}
break;
case 38:
//#line 206 "Parser.y"
{
						yyval.stmt = new Tree.Assign(val_peek(2).lvalue, val_peek(0).expr, val_peek(1).loc);
					}
break;
case 39:
//#line 210 "Parser.y"
{
                		yyval.stmt = new Tree.Exec(val_peek(0).expr, val_peek(0).loc);
                	}
break;
case 40:
//#line 214 "Parser.y"
{
                		yyval = new SemValue();
                	}
break;
case 42:
//#line 221 "Parser.y"
{
                		yyval = new SemValue();
                	}
break;
case 43:
//#line 227 "Parser.y"
{
						yyval.lvalue = new Tree.Ident(val_peek(1).expr, val_peek(0).ident, val_peek(0).loc);
						if (val_peek(1).loc == null) {
							yyval.loc = val_peek(0).loc;
						}
					}
break;
case 44:
//#line 234 "Parser.y"
{
                		yyval.lvalue = new Tree.Indexed(val_peek(3).expr, val_peek(1).expr, val_peek(3).loc);
                	}
break;
case 45:
//#line 240 "Parser.y"
{
						yyval.expr = new Tree.CallExpr(val_peek(4).expr, val_peek(3).ident, val_peek(1).elist, val_peek(3).loc);
						if (val_peek(4).loc == null) {
							yyval.loc = val_peek(3).loc;
						}
					}
break;
case 46:
//#line 249 "Parser.y"
{
                		yyval.expr = new Tree.Unary(Tree.PREINC, val_peek(0).lvalue, val_peek(1).loc);
                	}
break;
case 47:
//#line 253 "Parser.y"
{
                		yyval.expr = new Tree.Unary(Tree.PREDEC, val_peek(0).lvalue, val_peek(1).loc);
                	}
break;
case 48:
//#line 257 "Parser.y"
{
                		yyval.expr = new Tree.Unary(Tree.POSTINC, val_peek(1).lvalue, val_peek(0).loc);
                	}
break;
case 49:
//#line 261 "Parser.y"
{
                		yyval.expr = new Tree.Unary(Tree.POSTDEC, val_peek(1).lvalue, val_peek(0).loc);
                	}
break;
case 50:
//#line 265 "Parser.y"
{
						yyval.expr = val_peek(0).lvalue;
					}
break;
case 53:
//#line 271 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.PLUS, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 54:
//#line 275 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.MINUS, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 55:
//#line 279 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.MUL, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 56:
//#line 283 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.DIV, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 57:
//#line 287 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.MOD, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 58:
//#line 291 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.EQ, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 59:
//#line 295 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.NE, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 60:
//#line 299 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.LT, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 61:
//#line 303 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.GT, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 62:
//#line 307 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.LE, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 63:
//#line 311 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.GE, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 64:
//#line 315 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.AND, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 65:
//#line 319 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.OR, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 66:
//#line 323 "Parser.y"
{
                		yyval = val_peek(1);
                	}
break;
case 67:
//#line 327 "Parser.y"
{
                		yyval.expr = new Tree.Unary(Tree.NEG, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 68:
//#line 331 "Parser.y"
{
                		yyval.expr = new Tree.Unary(Tree.NOT, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 69:
//#line 335 "Parser.y"
{
                		yyval.expr = new Tree.Ternary(Tree.COND, val_peek(4).expr, val_peek(2).expr, val_peek(0).expr, val_peek(4).loc);
                	}
break;
case 70:
//#line 339 "Parser.y"
{
                		yyval.expr = new Tree.ReadIntExpr(val_peek(2).loc);
                	}
break;
case 71:
//#line 343 "Parser.y"
{
                		yyval.expr = new Tree.ReadLineExpr(val_peek(2).loc);
                	}
break;
case 72:
//#line 347 "Parser.y"
{
                		yyval.expr = new Tree.ThisExpr(val_peek(0).loc);
                	}
break;
case 73:
//#line 351 "Parser.y"
{
                		yyval.expr = new Tree.NewClass(val_peek(2).ident, val_peek(3).loc);
                	}
break;
case 74:
//#line 355 "Parser.y"
{
                		yyval.expr = new Tree.NewArray(val_peek(3).type, val_peek(1).expr, val_peek(4).loc);
                	}
break;
case 75:
//#line 359 "Parser.y"
{
                		yyval.expr = new Tree.TypeTest(val_peek(3).expr, val_peek(1).ident, val_peek(5).loc);
                	}
break;
case 76:
//#line 363 "Parser.y"
{
                		yyval.expr = new Tree.TypeCount(val_peek(1).ident, val_peek(3).loc);
                	}
break;
case 77:
//#line 367 "Parser.y"
{
                		yyval.expr = new Tree.TypeCast(val_peek(2).ident, val_peek(0).expr, val_peek(0).loc);
                	}
break;
case 78:
//#line 373 "Parser.y"
{
						yyval.expr = new Tree.Literal(val_peek(0).typeTag, val_peek(0).literal, val_peek(0).loc);
					}
break;
case 79:
//#line 377 "Parser.y"
{
						yyval.expr = new Null(val_peek(0).loc);
					}
break;
case 81:
//#line 384 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.elist = new ArrayList<Tree.Expr>();
                	}
break;
case 82:
//#line 391 "Parser.y"
{
						yyval.elist.add(val_peek(0).expr);
					}
break;
case 83:
//#line 395 "Parser.y"
{
                		yyval.elist = new ArrayList<Tree.Expr>();
						yyval.elist.add(val_peek(0).expr);
                	}
break;
case 84:
//#line 402 "Parser.y"
{
						yyval.stmt = new Tree.WhileLoop(val_peek(2).expr, val_peek(0).stmt, val_peek(4).loc);
					}
break;
case 85:
//#line 408 "Parser.y"
{
						yyval.stmt = new Tree.ForLoop(val_peek(6).stmt, val_peek(4).expr, val_peek(2).stmt, val_peek(0).stmt, val_peek(8).loc);
					}
break;
case 86:
//#line 414 "Parser.y"
{
						yyval.stmt = new Tree.Break(val_peek(0).loc);
					}
break;
case 87:
//#line 420 "Parser.y"
{
						yyval.stmt = new Tree.If(val_peek(3).expr, val_peek(1).stmt, val_peek(0).stmt, val_peek(5).loc);
					}
break;
case 88:
//#line 426 "Parser.y"
{
						yyval.stmt = val_peek(0).stmt;
					}
break;
case 89:
//#line 430 "Parser.y"
{
						yyval = new SemValue();
					}
break;
case 90:
//#line 436 "Parser.y"
{
						yyval.stmt = new Tree.Return(val_peek(0).expr, val_peek(1).loc);
					}
break;
case 91:
//#line 440 "Parser.y"
{
                		yyval.stmt = new Tree.Return(null, val_peek(0).loc);
                	}
break;
case 92:
//#line 446 "Parser.y"
{
						yyval.stmt = new Print(val_peek(1).elist, val_peek(3).loc);
					}
break;
case 93:
//#line 452 "Parser.y"
{
						yyval.stmt = new Tree.GuardedIf(val_peek(1).glist, val_peek(2).loc);
					}
break;
case 94:
//#line 458 "Parser.y"
{
						yyval.stmt = new Tree.GuardedDo(val_peek(1).glist, val_peek(2).loc);
					}
break;
case 95:
//#line 464 "Parser.y"
{
						yyval.glist.add(val_peek(0).stmt);
					}
break;
case 96:
//#line 468 "Parser.y"
{
						yyval.glist = new ArrayList<Tree>();
						yyval.glist.add(val_peek(0).stmt);
					}
break;
case 97:
//#line 475 "Parser.y"
{
						yyval.stmt = new Tree.Guarded(val_peek(2).expr, val_peek(0).stmt, val_peek(1).loc);
					}
break;
//#line 1356 "Parser.java"
//########## END OF USER-SUPPLIED ACTIONS ##########
    }//switch
    //#### Now let's reduce... ####
    //if (yydebug) debug("reduce");
    state_drop(yym);             //we just reduced yylen states
    yystate = state_peek(0);     //get new state
    val_drop(yym);               //corresponding value drop
    yym = yylhs[yyn];            //select next TERMINAL(on lhs)
    if (yystate == 0 && yym == 0)//done? 'rest' state and at first TERMINAL
      {
      //if (yydebug) debug("After reduction, shifting from state 0 to state "+YYFINAL+"");
      yystate = YYFINAL;         //explicitly say we're done
      state_push(YYFINAL);       //and save it
      val_push(yyval);           //also save the semantic value of parsing
      if (yychar < 0)            //we want another character?
        {
        yychar = yylex();        //get next character
        //if (yychar<0) yychar=0;  //clean, if necessary
        //if (yydebug)
          //yylexdebug(yystate,yychar);
        }
      if (yychar == 0)          //Good exit (if lex returns 0 ;-)
         break;                 //quit the loop--all DONE
      }//if yystate
    else                        //else not done yet
      {                         //get next state and push, for next yydefred[]
      yyn = yygindex[yym];      //find out where to go
      if ((yyn != 0) && (yyn += yystate) >= 0 &&
            yyn <= YYTABLESIZE && yycheck[yyn] == yystate)
        yystate = yytable[yyn]; //get new state
      else
        yystate = yydgoto[yym]; //else go to new defred
      //if (yydebug) debug("after reduction, shifting from state "+state_peek(0)+" to state "+yystate+"");
      state_push(yystate);     //going again, so push state & val...
      val_push(yyval);         //for next action
      }
    }//main loop
  return 0;//yyaccept!!
}
//## end of method parse() ######################################



//## run() --- for Thread #######################################
//## The -Jnorun option was used ##
//## end of method run() ########################################



//## Constructors ###############################################
//## The -Jnoconstruct option was used ##
//###############################################################



}
//################### END OF CLASS ##############################
