using System;
using MainClassNameSpace;
namespace Project_1025
{
    /*
        创建项目方式：
            1.创建一个文件夹
            2.命令行进入该文件夹，然后命令行输入：dotnet new Console 创建完毕
        运行文件方式：
            1.命令行：dotnet run
        开启代码补全：
            1.打开vscode按下：ctrl + shift + P 快捷键
            2.输入：OmniSharp: select project
            3.选择正确的项目（.sln文件）即可！
            4.它将正确读取csproj文件，智能提示等功能即可恢复！！！！
    */
    public abstract class Person
    {
        public abstract string Name { get; set; }
        public abstract int Age { get; set; }
    }
    public class Student : Person
    {
        
        string code = "code";
        public string Code { 
            get
            {
                return code;
            } 
            private set{
                code = value;
            } 
        }
        //这个与上面的区别 只是方便获得到一个属性 并且内部不做修改，但是可以设置属性的访问权限。
        public override string Name { get; set; } = "N.A";
        public override int Age { get; set; } = 0;
        public Student(){

        }
        public Student(string code,string name,int age){
            this.Code = code;
            this.Name = name;
            this.Age = age;
        }
        public override string ToString()
        {
            return $"Code:{Code},Name:{Name},Age:{Age}";
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            //Box box = new Box();
            var stu01 = new Student();
            System.Console.WriteLine($"Student Info:={stu01}");

            stu01.Age++;
            System.Console.WriteLine($"Student Info:={stu01}");
        }
    }
}
