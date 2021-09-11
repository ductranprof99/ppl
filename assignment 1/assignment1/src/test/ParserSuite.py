import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    def test_201(self):
        """
        successful test series
        """
        input_text = """class Test {
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 201))

    def test_202(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 202))

    def test_203(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            void aneue,onichann= 1213;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 203))

    def test_204(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            static void aneue,onichann= 1213;
            void innuedo() {
            
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 204))

    def test_204(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            static void aneue,onichann= 1213;
            void innuedo() {
                
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 204))

    def test_205(self):
        """
        successful test series
        """
        input_text = """class Test {
            int a = "addmaximum",b = 0001.18;
            static void aneue,onichann= 1213;
            void innuedo() {
            }
            Shape(float radius,width){
                             this.length := length;
                          this.width := width;
                 }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 205))

    def test_206(self):
        """
        successful test series
        """
        input_text = """class Test {
            static final int a = "addmaximum",b = 0001.18;
            static void aneue,onichann= 1213;
            void innuedo() {
                final int a = "addmaximum",b = 0001.18;
                void aneue,onichann= 1213;
            }
            Shape(float radius,width){
                             this.length := length;
                          this.width := width;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 206))

    def test_207(self):
        """
        successful test series
        """
        input_text = """class Test {
            static final int a = "addmaximum",b = 0001.18;
            static void aneue,onichann= 1213;
            void innuedo() {
                final int a = "addmaximum",b = 0001.18;
                void aneue,onichann= 1213;
                a := shiethole;
            }
            Shape(float radius,width){
                             this.length := length;
                          this.width := width;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 207))

    def test_208(self):
        """
        successful test series
        """
        input_text = """class Test {
                static final int a = "addmaximum",b = 0001.18;
                # static void aneue,onichann= {1,abc,sadf,0.0e25};
                void innuedo() {
                    final int a = "addmaximum",b = 0001.18;
                    # final testical = {1,"abc",3,0.0e25};
                    final testical notadipshit = {1,"abc",3,0.0e25};
                    void aneue,onichann = 1213;
                    a := shiethole;
                }
                Shape(float radius,width){
                                 this.length := length;
                              this.width := width;
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 208))

    def test_209(self):
        """
        successful test series
        """
        input_text = """class Test {
                static final int a = "addmaximum",b = 0001.18;
                final static int a = "addmaximum",b = 0001.18;
                # static void aneue,onichann= {1,abc,sadf,0.0e25};
                void innuedo() {
                    final int a = "addmaximum",b = 0001.18;
                    # final testical = {1,"abc",3,0.0e25};
                    int[10] testical = {1,"abc",3,0.0e25};
                    void aneue,onichann = 1213;
                    a := shiethole;
                }
                Shape(float radius,width){
                    this.length := length;
                    this.width := width;
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 209))

    def test_210(self):
        """
        successful test series
        """
        input_text = """
            class foo {
                type[7857] n = this.Shape(x.foo(5)[4]*(!m) + (s >= m || m+-n));
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 210))

    def test_211(self):
        """
        successful test series
        """
        input_text = """
            class foo {
                H[5] function(A a,b,c; H n){
                    (5+6).adopt := method.avocation(nein,nein,nein);
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 211))

    def test_212(self):
        """
        successful test series
        """
        input_text = """
            class foo {
                H[5] function(A a,b,c; H n){
                    (5+6).adopt := ((((((((1))))))));
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 212))

    def test_213(self):
        """
        successful test series
        """
        input_text = """
            class foo {
                H[5] function(A a,b,c; H n){
                    (x.foo(5)[4]*(!m) + (s >= m || m+-n)).adopt := a.b.c(x.foo(5)[4]*(!m) + (s >= m || m+-n),x.foo(5)[4]*(!m) + (s >= m || m+-n)).b.c.a;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 213))

    def test_214(self):
        """
        successful test series
        """
        input_text = """
        class foo {
            H[5] function(A a,b,c; H n){
                (x.foo(5)[4]*(!m) + (s >= m || m+-n))[1].adopt := a.b.c(x.foo(5)[4]*(!m) + (s >= m || m+-n),x.foo(5)[4]*(!m) + (s >= m || m+-n)).b.c.a;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 214))

    def test_215(self):
        """
        successful test series
        """
        input_text = """
        class foo {
            H[5] function(A a,b,c; H n){
                (x.foo(5)[4]*(!m) + (s >= m || m+-n))[x.foo(5)[4]*(!m) + (s >= m || m+-n)].adopt[x.foo(5)[4]*(!m) + (s >= m || m+-n).asdfadf] := a.b.c(x.foo(5)[4]*(!m) + (s >= m || m+-n),x.foo(5)[4]*(!m) + (s >= m || m+-n)).b.c.a;
                
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 215))

    def test_216(self):
        """
        successful test series
        """
        input_text = """
        class foo {
            H[5] function(A a,b,c; H n){
                (x.foo(5)[4]*(!m) + (s >= m || m+-n))[x.foo(5)[4]*(!m) + (s >= m || m+-n)].adopt[x.foo(5)[4]*(!m) + (s >= m || m+-n).asdfadf.b[12].a.c] := exp;
                # test fail a.b.c.d
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 216))

    def test_11(self):
        """
        successful test series
        """
        input_text = """
        class program {
            int b = 2;
            int[5] a = {1, 2, 3, 4, 5};
            int c = b*a[0; 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input_text, expect, 217))

    def test_9(self):
        """
        syntax error test series
        """
        input_text = """class QuotientRemainder {
                       static void main(string[2] args) {
                            5+5 := y;
                        }
                    }"""
        expect = ""
        self.assertTrue(TestParser.test(input_text, expect, 299))

    def test_10(self):
        """
        syntax error test series
        """
        input_text = """class Example1 {
                    int factorial(int n){ {}
                    int y = 20;
                    if n == 0 then return 1; else return n * this.factorial(n - 1);
                    }
                    void main(){
                    int x;
                    x := io.readInt();
                    io.writeIntLn(this.factorial(x));
                    }
                    }"""
        expect = ""
        self.assertTrue(TestParser.test(input_text, expect, 300))

    # def test_287(self):
    #     input_text = """class QuotientRemainder {
    #                     static void main(string[2] args) {
    #
    #                         System.out.println("Quotient = " + quotient);
    #                         System.out.println("Remainder = " + remainder);
    #                     }
    #                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input_text, expect, 210))
    #
    # def test_288(self):
    #     input_text = """class Shape {
    #                     float length,width;
    #                     float getArea() {}
    #                     Shape(float length,width){
    #                         this.length := length;
    #                         this.width := width;
    #                     }
    #                 }
    #                 class Rectangle extends Shape {
    #                     float getArea(){
    #                         return this.length*this.width;
    #                     }
    #                 }
    #                 class Triangle extends Shape {
    #                     float getArea(){
    #                         return this.length*this.width / 2;
    #                     }
    #                 }
    #                 class Example2 {
    #                     void main(){
    #                         Exam[2] x = {1.2, 3.4, 5};
    #                         Shape s = new Rectangle(3,4);
    #                         io.writeFloatLn(s.getArea());
    #                         s := 2+3-95*74;
    #                         io.writeFloatLn(s.getArea());
    #                         y := {1.2 ,2, 3};
    #                         a > this.a.a := 5;
    #                         return a;
    #                     }
    #                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input_text, expect, 209))
    #
    # def test289(self):
    #     input_text = """class SHap {
    #         int get() {
    #             a := b[3 - foo(2)];
    #         }
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input_text, expect, 245))
    # def test_291(self):
    #     input_text = """class ABC { }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input_text, expect, 201))
    #
    # def test_292(self):
    #     input_text = """class ABC extends { }"""
    #     expect = "Error on line 1 col 18: {"
    #     self.assertTrue(TestParser.test(input_text, expect, 202))
    #
    # def test_293(self):
    #     input_text = """class { }"""
    #     expect = "Error on line 1 col 6: {"
    #     self.assertTrue(TestParser.test(input_text, expect, 203))
    #
    # def test_294(self):
    #     input_text = """class ABC }"""
    #     expect = "Error on line 1 col 10: }"
    #     self.assertTrue(TestParser.test(input_text, expect, 204))
    #
    # def test_295(self):
    #     input_text = """class Shape {
    #                     static final int numOfShape = 0;
    #                     final int immuAttribute = 0;
    #                     float length,width;
    #                     static int getNumOfShape() {
    #                         return numOfShape;
    #                     }
    #                 }
    #                 class Rectangle extends Shape {
    #                     float getArea(){
    #                         return this.length*this.width;
    #                     }
    #                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input_text, expect, 205))
    #
    # def test_296(self):
    #     input_text = """class Shape {
    #                     static final int numOfShape = 0;
    #                     final int immuAttribute = 0;
    #                     float length,width;
    #                     static int getNumOfShape() {
    #                         return numOfShape;
    #                     }
    #                 }
    #                 class Rectangle extends Shape {
    #                     float getArea(){
    #                         return this.length*this.width;
    #                     }
    #                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input_text, expect, 206))
    #
    # def test_297(self):
    #     input_text = """class Example2 extends ABC {
    #                     int length,width;
    #                     float getArea() {}
    #                     Shape(float length,width){
    #                         this.length := length;
    #                         this.width := width;
    #                     }
    #                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input_text, expect, 207))
    #
    # def test_298(self):
    #     input_text = """class Example1 {
    #                     void main(){
    #                         int x;
    #                         l[3] := 2*value*2/2-c;
    #                         x := io.readInt();
    #                         io.writeIntLn(this.factorial(x));
    #                     }
    #                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input_text, expect, 208))
    #
    # def test_300(self):
    #     input_text = """class Shape {
    #                     float length,width;
    #                     float getArea() {}
    #                     Shape(float length,width){
    #                         this.length := length;
    #                         this.width := width;
    #                     }
    #                 }
    #             """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input_text, expect, 209))
