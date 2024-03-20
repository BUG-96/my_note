[TOC]



## javaScript简介



### JavaScript：直接写入HTML输出流



```javascript
<body>
<p>
JavaScript 能够直接写入 HTML 输出流中：
</p>
<script>
document.write("<h1>这是我丢标题</h1>");
document.write("<p>这是一个段落。</p>");
</script>
<p>
您只能在 HTML 输出流中使用 <strong>document.write</strong>。
如果您在文档已加载后使用它（比如在函数中），会覆盖整个文档。
</p>
</body>
</html>
```



### JavaScript：对事件的反应

<button type="button" onclick="alert('欢迎!')">点我!</button>

<img src="E:\课程笔记\pic\image-20240311155735394.png" alt="image-20240311155735394" style="zoom:33%;" />





### JavaScript：改变 HTML 内容

```
x=document.getElementById("demo");  //查找元素
x.innerHTML="Hello JavaScript";    //改变内容
```

```
<!DOCTYPE html>
<html>
<head> 
<meta charset="utf-8"> 
<title>菜鸟教程(runoob.com)</title> 
</head>
<body>
	
<h1>我的第一段 JavaScript</h1>
<p id="demo">
JavaScript 能改变 HTML 元素的内容。
</p>
<script>
function myFunction()
{
	x=document.getElementById("demo");  // 找到元素
	x.innerHTML="Hello JavaScript!";    // 改变内容
}
</script>
<button type="button" onclick="myFunction()">点击这里</button>
	
</body>
</html>
```



### JavaScript：改变 HTML 图像

```
<body>
	
<script>
function changeImage()
{
	element=document.getElementById('myimage')
	if (element.src.match("bulbon"))
	{
		element.src="/images/pic_bulboff.gif";
	}
	else
	{
		element.src="/images/pic_bulbon.gif";
	}
}
</script>
<img id="myimage" onclick="changeImage()" src="/images/pic_bulboff.gif" width="100" height="180">
<p>点击灯泡就可以打开或关闭这盏灯</p>
	
</body>
```



### JavaScript：改变 HTML 样式

```
<body>
	
<h1>我的第一段 JavaScript</h1>
<p id="demo">
JavaScript 能改变 HTML 元素的样式。
</p>
<script>
function myFunction()
{
	x=document.getElementById("demo") // 找到元素
	x.style.color="#ff0000";          // 改变样式
}
</script>
<button type="button" onclick="myFunction()">点击这里</button>
	
</body>
```



### JavaScript：验证输入
```
<body>
	
<h1>我的第一段 JavaScript</h1>
<p>请输入数字。如果输入值不是数字，浏览器会弹出提示框。</p>
<input id="demo" type="text">
<script>
function myFunction()
{
	var x=document.getElementById("demo").value;
	if(x==""||isNaN(x))
	{
		alert("不是数字");
	}
}
</script>
<button type="button" onclick="myFunction()">点击这里</button>
	
</body>
```

## JavaScript用法

HTML 中的 Javascript 脚本代码必须位于 **<script>** 与 **</script>** 标签之间。

Javascript 脚本代码可被放置在 HTML 页面的 **<body>** 和 **<head>** 部分中。



## < head >  中的 JavaScript 函数

```
<!DOCTYPE html>
<html>
<head>
<script>
function myFunction()
{
    document.getElementById("demo").innerHTML="我的第一个 JavaScript 函数";
}
</script>
</head>
<body>
<h1>我的 Web 页面</h1>
<p id="demo">一个段落</p>
<button type="button" onclick="myFunction()">尝试一下</button>
</body>
</html>
```

## < body> 中的 JavaScript 函数

```
<!DOCTYPE html>
<html>
<body>
<h1>我的 Web 页面</h1>
<p id="demo">一个段落</p>
<button type="button" onclick="myFunction()">尝试一下</button>
<script>
function myFunction()
{
    document.getElementById("demo").innerHTML="我的第一个 JavaScript 函数";
}
</script>
</body>
</html>
```



## 外部的 JavaScript

也可以把脚本保存到外部文件中。外部文件通常包含被多个网页使用的代码。

外部 JavaScript 文件的文件扩展名是 .js。

如需使用外部文件，请在 <script> 标签的 "src" 属性中设置该 .js 文件：

## 实例

```
<!DOCTYPE html>
<html>
<body>
<script src="myScript.js"></script>
</body>
</html>
```

你可以将脚本放置于 <head> 或者 <body>中，放在 <script> 标签中的脚本与外部引用的脚本运行效果完全一致。

myScript.js 文件代码如下：

```
function myFunction()
{
    document.getElementById("demo").innerHTML="我的第一个 JavaScript 函数";
}
```



## JavaScript 输出

JavaScript 没有任何打印或者输出的函数。



## JavaScript 显示数据

JavaScript 可以通过不同的方式来输出数据：

-   使用 **window.alert()** 弹出警告框。
-   使用 **document.write()** 方法将内容写到 HTML 文档中。
-   使用 **innerHTML** 写入到 HTML 元素。
-   使用 **console.log()** 写入到浏览器的控制台。

```
<script>
window.alert(5 + 6);
</script>
```



```
<body>
	
<h1>我的第一个 Web 页面</h1>
<p id="demo">我的第一个段落。</p>
<script>
document.getElementById("demo").innerHTML="段落已修改。";
</script>
	
</body>
```

```
<body>
	
<h1>我的第一个 Web 页面</h1>
<p>我的第一个段落。</p>
<script>
document.write(Date());
</script>
	
</body>
```

```
<body>
	
<h1>我的第一个 Web 页面</h1>
<p>
浏览器中(Chrome, IE, Firefox) 使用 F12 来启用调试模式， 在调试窗口中点击 "Console" 菜单。
</p>
<script>
a = 5;
b = 6;
c = a + b;
console.log(c);
</script>
	
</body>
```



## JavaScript语法



## JavaScript 字面量

在编程语言中，一般固定值称为字面量，如 3.14。

**数字（Number）字面量** 可以是整数或者是小数，或者是科学计数(e)。

3.14

**字符串（String）字面量** 可以使用单引号或双引号:

"John Doe"

**表达式字面量** 用于计算：

5 + 6

**数组（Array）字面量** 定义一个数组：

[40, 100, 1, 5, 25, 10]

**对象（Object）字面量** 定义一个对象：

{firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"}

**函数（Function）字面量** 定义一个函数：

function myFunction(a, b) { return a * b;}



## JavaScript 变量

在编程语言中，变量用于存储数据值。

JavaScript 使用关键字 **var** 来定义变量， 使用等号来为变量赋值：

```
var x, length

x = 5

length = 6
```

## JavaScript 操作符

JavaScript使用 **算术运算符** 来计算值:

(5 + 6) * 10

## JavaScript 关键字

JavaScript 关键字用于标识要执行的操作。

和其他任何编程语言一样，JavaScript 保留了一些关键字为自己所用。

**var** 关键字告诉浏览器创建一个新的变量：

var x = 5 + 6;
var y = x * 10;

JavaScript 同样保留了一些关键字，这些关键字在当前的语言版本中并没有使用，但在以后 JavaScript 扩展中会用到。

以下是 JavaScript 中最重要的保留关键字（按字母顺序）：



| abstract |    else    | instanceof |    super     |
| :------: | :--------: | :--------: | :----------: |
| boolean  |    enum    |    int     |    switch    |
|  break   |   export   | interface  | synchronized |
|   byte   |  extends   |    let     |     this     |
|   case   |   false    |    long    |    throw     |
|  catch   |   final    |   native   |    throws    |
|   char   |  finally   |    new     |  transient   |
|  class   |   float    |    null    |     true     |
|  const   |    for     |  package   |     try      |
| continue |  function  |  private   |    typeof    |
| debugger |    goto    | protected  |     var      |
| default  |     if     |   public   |     void     |
|  delete  | implements |   return   |   volatile   |
|    do    |   import   |   short    |    while     |
|  double  |     in     |   static   |     with     |



## JavaScript 语句标识符

JavaScript 语句通常以一个 **语句标识符** 为开始，并执行该语句。

语句标识符是保留关键字不能作为变量名使用。

下表列出了 JavaScript 语句标识符 (关键字) ：

| 语句         | 描述                                                         |
| :----------- | :----------------------------------------------------------- |
| break        | 用于跳出循环。                                               |
| catch        | 语句块，在 try 语句块执行出错时执行 catch 语句块。           |
| continue     | 跳过循环中的一个迭代。                                       |
| do ... while | 执行一个语句块，在条件语句为 true 时继续执行该语句块。       |
| for          | 在条件语句为 true 时，可以将代码块执行指定的次数。           |
| for ... in   | 用于遍历数组或者对象的属性（对数组或者对象的属性进行循环操作）。 |
| function     | 定义一个函数                                                 |
| if ... else  | 用于基于不同的条件来执行不同的动作。                         |
| return       | 退出函数                                                     |
| switch       | 用于基于不同的条件来执行不同的动作。                         |
| throw        | 抛出（生成）错误 。                                          |
| try          | 实现错误处理，与 catch 一同使用。                            |
| var          | 声明一个变量。                                               |
| while        | 当条件语句为 true 时，执行语句块。                           |



# JavaScript 数据类型

------

**值类型(基本类型)**：字符串（String）、数字(Number)、布尔(Boolean)、空（Null）、未定义（Undefined）、Symbol。

**引用数据类型（对象类型）**：对象(Object)、数组(Array)、函数(Function)，还有两个特殊的对象：正则（RegExp）和日期（Date）。

<img src="E:\课程笔记\pic\JavaScript笔记\image-20240313170640391.png" alt="image-20240313170640391" style="zoom:50%;" />

## JavaScript 拥有动态类型

JavaScript 拥有动态类型。这意味着相同的变量可用作不同的类型：

## 实例

var x;        // x 为 undefined
var x = 5;      // 现在 x 为数字
var x = "John";   // 现在 x 为字符串

变量的数据类型可以使用 **typeof** 操作符来查看：

## 实例

**typeof** "John"         *// 返回 string*
**typeof** 3.14          *// 返回 number*
**typeof** **false**         *// 返回 boolean*
**typeof** [1,2,3,4]       *// 返回 object*
**typeof** {name:'John', age:34} *// 返回 object*

## JavaScript 字符串

字符串是存储字符（比如 "Bill Gates"）的变量。

字符串可以是引号中的任意文本。您可以使用单引号或双引号：

```
var carname="Volvo XC60";
var carname='Volvo XC60';
```

## JavaScript 数字

JavaScript 只有一种数字类型。数字可以带小数点，也可以不带：

## 实例

var x1=34.00;   //使用小数点来写
var x2=34;     //不使用小数点来写

## JavaScript 布尔

布尔（逻辑）只能有两个值：true 或 false。

var x=true;

## JavaScript 数组

下面的代码创建名为 cars 的数组：

```
var cars=new Array();
cars[0]="Saab";

或者 (condensed array):

var cars=new Array("Saab","Volvo","BMW");
```

## JavaScript 对象

对象由花括号分隔。在括号内部，对象的属性以名称和值对的形式 (name : value) 来定义。属性由逗号分隔：

```
var person={firstname:"John", lastname:"Doe", id:5566};
```

上面例子中的对象 (person) 有三个属性：firstname、lastname 以及 id。

空格和折行无关紧要。声明可横跨多行：

```
var person={
    firstname : "John",
    lastname : "Doe",
    id: 5566
};
```
对象属性有两种寻址方式：
```javascript
<script>
    var person=
    {
        firstname : "John",
        lastname  : "Doe",
        id        :  5566
    };
    document.write(person.lastname + "<br>");
    document.write(person["lastname"] + "<br>");
</script>
```

## Undefined 和 Null

Undefined 这个值表示变量不含有值。

可以通过将变量的值设置为 null 来清空变量。

## 实例

```
cars=null;
person=null;
```

## 声明变量类型

当您声明新变量时，可以使用关键词 "new" 来声明其类型：

```
var carname=new String;
var x=   new Number;
var y=   new Boolean;
var cars=  new Array;
var person= new Object;
```

# JavaScript 对象

------

JavaScript 对象是拥有属性和方法的数据。

## JavaScript 对象

在 JavaScript中，几乎所有的事物都是对象。



| ![Note](https://kurby-pic.oss-cn-shanghai.aliyuncs.com/Pic/lamp.jpg) | 在 JavaScript 中，对象是非常重要的，当你理解了对象，就可以了解 JavaScript 。 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |



你已经学习了 JavaScript 变量的赋值。

以下代码为变量 **car** 设置值为 "Fiat" :

var car = "Fiat";

对象也是一个变量，但对象可以包含多个值（多个变量），每个值以 **name:value** 对呈现。

var car = {name:"Fiat", model:500, color:"white"};

在以上实例中，3 个值 ("Fiat", 500, "white") 赋予变量 car。

| ![Note](https://www.runoob.com/images/lamp.jpg) | JavaScript 对象是变量的容器。 |
| ----------------------------------------------- | ----------------------------- |
|                                                 |                               |



------

## 对象属性

可以说 "JavaScript 对象是变量的容器"。

但是，我们通常认为 "JavaScript 对象是键值对的容器"。

键值对通常写法为 **name : value** (键与值以冒号分割)。

键值对在 JavaScript 对象通常称为 **对象属性**。



| ![Note](https://kurby-pic.oss-cn-shanghai.aliyuncs.com/Pic/lamp.jpg) | JavaScript 对象是属性变量的容器。 |
| ------------------------------------------------------------ | --------------------------------- |
|                                                              |                                   |



对象键值对的写法类似于：

-   PHP 中的关联数组
-   Python 中的字典
-   C 语言中的哈希表
-   Java 中的哈希映射
-   Ruby 和 Perl 中的哈希表

## 访问对象属性

你可以通过两种方式访问对象属性:

## 实例 1

```
person.lastName;
```

## 实例 2

```
person["lastName"];
```

## 对象方法

对象的方法定义了一个函数，并作为对象的属性存储。

对象方法通过添加 () 调用 (作为一个函数)。

该实例访问了 person 对象的 fullName() 方法:

## 实例

```
name = person.fullName();
```

```
<script>
var person = {
    firstName: "John",
    lastName : "Doe",
    id : 5566,
    fullName : function() 
	{
       return this.firstName + " " + this.lastName;
    }
};
document.getElementById("demo1").innerHTML = "不加括号输出函数表达式："  + person.fullName;
document.getElementById("demo2").innerHTML = "加括号输出函数执行结果："  +  person.fullName();
</script>

输出结果：
创建和使用对象方法。
对象方法是一个函数定义,并作为一个属性值存储。
不加括号输出函数表达式：function() { return this.firstName + " " + this.lastName; }
加括号输出函数执行结果：John Doe
```

| ![Note](https://www.runoob.com/images/lamp.jpg) | JavaScript 对象是属性和方法的容器。                      |
| ----------------------------------------------- | -------------------------------------------------------- |
|                                                 | 在随后的教程中你将学习到更多关于函数，属性和方法的知识。 |

## 访问对象方法

你可以使用以下语法创建对象方法：

```
methodName : function() {
    // 代码 
}
```

你可以使用以下语法访问对象方法：



# JavaScript 函数

------

函数是由事件驱动的或者当它被调用时执行的可重复使用的代码块。

## 实例

```
objectName.methodName()
```

```
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>测试实例</title>
<script>
function myFunction()
{
    alert("Hello World!");
}
</script>
</head>
 
<body>
<button onclick="myFunction()">点我</button>
</body>
</html>
```

## JavaScript 函数语法

函数就是包裹在花括号中的代码块，前面使用了关键词 function：

function *functionname*()
{
  *// 执行代码*
}

当调用该函数时，会执行函数内的代码。

可以在某事件发生时直接调用函数（比如当用户点击按钮时），并且可由 JavaScript 在任何位置进行调用。

| ![lamp](https://kurby-pic.oss-cn-shanghai.aliyuncs.com/Pic/lamp.jpg) | JavaScript 对大小写敏感。关键词 function 必须是小写的，并且必须以与函数名称相同的大小写来调用函数。 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

## 调用带参数的函数

在调用函数时，您可以向其传递值，这些值被称为参数。

这些参数可以在函数中使用。

您可以发送任意多的参数，由逗号 (,) 分隔：

```
myFunction(*argument1,argument2*)
```

当您声明函数时，请把参数作为变量来声明：

```
function myFunction(***var1***,***var2***)
{
	代码
}
```

变量和参数必须以一致的顺序出现。第一个变量就是第一个被传递的参数的给定的值，以此类推。



```
<body>

<p>点击这个按钮，来调用带参数的函数。</p>
<button onclick="myFunction('Harry Potter','Wizard')">点击这里</button>
<script>
function myFunction(name,job){
	alert("Welcome " + name + ", the " + job);
}
</script>

</body>
```

## 带有返回值的函数

有时，我们会希望函数将值返回调用它的地方。

通过使用 return 语句就可以实现。

在使用 return 语句时，函数会停止执行，并返回指定的值。

### 语法

```
function myFunction()
{
  var x=5;
  return x;
}
```

上面的函数会返回值 5。

**注意：** 整个 JavaScript 并不会停止执行，仅仅是函数。JavaScript 将继续执行代码，从调用函数的地方。

函数调用将被返回值取代：

```
var myVar=myFunction();
```

myVar 变量的值是 5，也就是函数 "myFunction()" 所返回的值。

即使不把它保存为变量，您也可以使用返回值：

```
document.getElementById("demo").innerHTML=myFunction();

"demo" 元素的 innerHTML 将成为 5，也就是函数 "myFunction()" 所返回的值。
```

您可以使返回值基于传递到函数中的参数：

## 实例

计算两个数字的乘积，并返回结果：

```
function myFunction(a,b) {    return a*b; }  document.getElementById("demo").innerHTML=myFunction(4,3);

"demo" 元素的 innerHTML 将是：

12
```

在您仅仅希望退出函数时 ，也可使用 return 语句。返回值是可选的：

```
function myFunction(a,b) 
{    
	if (a>b)    
	{        
		return;    
	}    
	x=a+b 
}
```

如果 a 大于 b，则上面的代码将退出函数，并不会计算 a 和 b 的总和。

## 局部 JavaScript 变量

在 JavaScript 函数内部声明的变量（使用 var）是*局部*变量，所以只能在函数内部访问它。（该变量的作用域是局部的）。

您可以在不同的函数中使用名称相同的局部变量，因为只有声明过该变量的函数才能识别出该变量。

只要函数运行完毕，本地变量就会被删除。

------

## 全局 JavaScript 变量

在函数外声明的变量是*全局*变量，网页上的所有脚本和函数都能访问它。

------

## JavaScript 变量的生存期

JavaScript 变量的生命期从它们被声明的时间开始。

局部变量会在函数运行以后被删除。

全局变量会在页面关闭后被删除。

## 向未声明的 JavaScript 变量分配值

如果您把值赋给尚未声明的变量，该变量将被自动作为 window 的一个属性。

这条语句：

carname="Volvo";

将声明 window 的一个属性 carname。

非严格模式下给未声明变量赋值创建的全局变量，是全局对象的可配置属性，可以删除。

```
var var1 = 1; // 不可配置全局属性
var2 = 2; // 没有使用 var 声明，可配置全局属性

console.log(this.var1); // 1
console.log(window.var1); // 1
console.log(window.var2); // 2

delete var1; // false 无法删除
console.log(var1); //1

delete var2; 
console.log(delete var2); // true
console.log(var2); // 已经删除 报错变量未定义
```

# JavaScript 作用域

------

作用域是可访问变量的集合。

------

## JavaScript 作用域

在 JavaScript 中, 对象和函数同样也是变量。

**在 JavaScript 中, 作用域为可访问变量，对象，函数的集合。**

JavaScript 函数作用域: 作用域在函数内修改。

------

## JavaScript 局部作用域

变量在函数内声明，变量为局部变量，具有局部作用域。

局部变量：只能在函数内部访问。

## 实例

```
// 此处不能调用 carName 变量 function myFunction() {    var carName = "Volvo";    // 函数内可调用 carName 变量 }
```



## JavaScript 全局变量

变量在函数外定义，即为全局变量。

全局变量有 **全局作用域**: 网页中所有脚本和函数均可使用。 

## 实例

```
var carName = " Volvo";  // 此处可调用 carName 变量 function myFunction() {    // 函数内可调用 carName 变量 }
```

如果变量在函数内没有声明（没有使用 var 关键字），该变量为全局变量。

以下实例中 carName 在函数内，但是为全局变量。

## 实例

```
// 此处可调用 carName 变量  
function myFunction() 
{    
    carName = "Volvo";     // 此处可调用 carName 变量 
}
```

## 你知道吗?



| ![Note](https://kurby-pic.oss-cn-shanghai.aliyuncs.com/Pic/lamp.jpg) | 你的全局变量，或者函数，可以覆盖 window 对象的变量或者函数。 局部变量，包括 window 对象可以覆盖全局变量和函数。 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

在 JavaScript 中，函数内部的局部变量通常不可以直接被外部作用域访问，但有几种方式可以将函数内的局部变量暴露给外部作用域，具体如下：

-   **通过全局对象：**在函数内部，可以通过将局部变量赋值给 window 对象的属性来使其成为全局可访问的。例如，使用 **window.a = a;** 语句，可以在函数外部通过 **window.a** 访问到这个局部变量的值。
-   **定义全局变量：**在函数内部不使用 **var、let** 或 **const** 等关键字声明变量时，该变量会被视为全局变量，从而可以在函数外部访问。但这种做法通常不推荐，因为它可能导致意外的副作用和代码难以维护。
-   **返回值：**可以通过在函数内部使用 **return** 语句返回局部变量的值，然后在函数外部接收这个返回值。这样，虽然局部变量本身不会被暴露，但其值可以通过函数调用传递到外部。
-   **闭包：**JavaScript 中的闭包特性允许内部函数访问外部函数的局部变量。即使外部函数执行完毕后，其局部变量仍然可以被内部函数引用。
-   **属性和方法：**定义在全局作用域中的变量和函数都会变成 window 对象的属性和方法，因此可以在调用时省略 window，直接使用变量名或函数名。

# JavaScript 事件

HTML 事件是发生在 HTML 元素上的事情。

当在 HTML 页面中使用 JavaScript 时， JavaScript 可以触发这些事件。

------

## HTML 事件

HTML 事件可以是浏览器行为，也可以是用户行为。

以下是 HTML 事件的实例：

-   HTML 页面完成加载
-   HTML input 字段改变时
-   HTML 按钮被点击

通常，当事件发生时，你可以做些事情。

在事件触发时 JavaScript 可以执行一些代码。

HTML 元素中可以添加事件属性，使用 JavaScript 代码来添加 HTML 元素。

单引号:

```
<some-HTML-element some-event='JavaScript 代码'>
```

双引号:

```
<some-HTML-element some-event="JavaScript 代码">
```

```
<body>
<button onclick="getElementById('demo').innerHTML=Date()">现在的时间是?</button>
<p id="demo"></p>
```

以上实例中，JavaScript 代码将修改 id="demo" 元素的内容。

在下一个实例中，代码将修改自身元素的内容 (使用 **this**.innerHTML):

```
<body>

<button onclick="this.innerHTML=Date()">现在的时间是?</button>

</body>
```

## 常见的HTML事件

下面是一些常见的HTML事件的列表:

| 事件        | 描述                                 |
| :---------- | :----------------------------------- |
| onchange    | HTML 元素改变                        |
| onclick     | 用户点击 HTML 元素                   |
| onmouseover | 鼠标指针移动到指定的元素上时发生     |
| onmouseout  | 用户从一个 HTML 元素上移开鼠标时发生 |
| onkeydown   | 用户按下键盘按键                     |
| onload      | 浏览器已完成页面的加载               |

## avaScript 可以做什么?

事件可以用于处理表单验证，用户输入，用户行为及浏览器动作:

-   页面加载时触发事件
-   页面关闭时触发事件
-   用户点击按钮执行动作
-   验证用户输入内容的合法性
-   等等 ...

可以使用多种方法来执行 JavaScript 事件代码：

-   HTML 事件属性可以直接执行 JavaScript 代码
-   HTML 事件属性可以调用 JavaScript 函数
-   你可以为 HTML 元素指定自己的事件处理程序
-   你可以阻止事件的发生。
-   等等 ...

# JavaScript 字符串

JavaScript 字符串用于存储和处理文本。

## JavaScript 字符串

字符串可以存储一系列字符，如 "John Doe"。

字符串可以是插入到引号中的任何字符。你可以使用单引号或双引号：

## 实例

var carname = "Volvo XC60";
var carname = 'Volvo XC60';











































