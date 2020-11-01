using System;
namespace MainClassNameSpace
{
    class Box
    {
       public double length;   // 长度
       public double breadth;  // 宽度
       public double height;   // 高度

       public Box(){
           Console.Write("构造函数");
       }


        //C# 是有自动垃圾GC回收机制的
       ~Box(){
           Console.Write("析构函数");
       }
    }
}