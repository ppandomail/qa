# XPath

* XML Path Language
* Es un lenguaje que permite construir expresiones que recorren y procesan un documento XML.
* Permite buscar y seleccionar la ubicación de cualquier elemento en una página web utilizando la estructura HTML.
* En Selenium, si los locators generales como id, class, name, etc. no encuentran los elementos, se utiliza XPath para encontrar un elemento en la página web.
* Es una ruta XML utilizada para navegar a través de la estructura HTML de la página.
* Para practicar: [Xpath Diner](https://topswagcode.com/xpath/)

## Uso

1. Chrome
1. Fn + F12 -> Solapa 'Elementos' -> CTRL + F

## Formato básico

    ```xpath
    //tagname[@attribute='value']
    ```

* //: selecciona el nodo actual
* tagname: tagname del nodo en particular, como input, div, img, etc.
* @: seleccionar atributo
* attribute: nombre del atributo del nodo, como id, name, class, etc.
* value: valor del atributo

## Tipos de XPath

* XPath absoluto:
  * Utiliza la ruta completa desde el elemento raíz hasta el elemento deseado.
  * Es la forma directa de encontrar el elemento, pero la desventaja es que si se realizan cambios en la ruta del elemento, XPath falla.

        ```xpath
        /html/body/div[1]/section/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[1]/div/h4[1]/b
        /html/body/main/div/div/div/div/div[1]/div/form/div/input
        ```

* XPath relativo:
  * Puede buscar elementos en cualquier parte de la página web, lo que significa que no es necesario escribir un xpath largo y puede comenzar desde el medio de la estructura HTML DOM.
  * Siempre se prefiere el Xpath relativo, ya que no es una ruta completa desde el elemento raíz.

        ```xpath
        //*[@id="F1:username"]
        //*[@class='featured-box']//*[text()='Testing']

        ```

## Selección de nodos

| Sintaxis | Descripción |
| --- | --- |
| /   | Selecciona desde el nodo raiz |
| //  | Selecciona nodos desde el nodo contextual (sin importar donde se encuentren) |
| .   | Selecciona el nodo contextual |
| ..  | Selecciona el padre del nodo contextual |
| nom | Selecciona los nodos hijos del nodo nombrado |
| @att| Selecciona todos los atributos 'att' |

Estas serian las formas de poder seleccionar nodos que no se conocen

| Sintaxis | Descripción |
| --- | --- |
| //*   | Selecciona todos los nodos del documento |
| *     | Selecciona todos los nodos elemento |
| @*    | Selecciona todos los nodos atributos |
| //ej/*| Selecciona todos los nodos hijos del nodo ejemplo |
| //ej[@*] | Selecciona todos los atributos del nodo ejemplo |

## Como escribir XPath dinámico en Selenium Webdriver

### XPath básico

    ```xpath
    //input[@type='text']
    //label[@id='message23']
    //input[@value='RESET']
    //*[@class='barone']
    //a[@href='http://demo.guru99.com/']
    //img[@src='//guru99.com/images/home/java.png']
    ```

### Función contains

    ```xpath
    //*[contains(@type,'sub')]
    //*[contains(@name,'btn')]
    //*[contains(@id,'message')]
    //*[contains(text(),'here')]
    //*[contains(@href,'guru99.com')]
    ```

### Uso OR y AND

    ```xpath
    //*[@type='submit' or @name='btnReset']
    //input[@type='submit' and @name='btnLogin']
    ```

### Función starts-with

    ```xpath
    //label[starts-with(@id,'message')]
    ```

### Función text

    ```path
    //td[text()='UserID']
    ```

### Función not

    ```path
    //h1[not(contains(text(),'Facturador'))]
    ```

### Función last

    ```path
    //input[@type='text'])[last()]
    ```

### Métodos de ejes

* Se utilizan para encontrar elementos complejos o dinámicos

#### following

    ```xpath
    //*[@type='text']//following::input
    ```

#### ancestor

* El padre de un nodo, el padre del padre, etc.

        ```xpath
        //*[texto()='Prueba empresarial']//ancestor::div
        ```

#### child

* Los nodos pueden tener 0, 1 o más hijos.

        ```xpath
        //*[@id='java_technologies']//child::li
        ```

#### preceding

    ```xpath
    //*[@type='submit']//preceding::input
    ```

#### following-sibling

* Nodos que tiene el mismo padre

        ```xpath
        //*[@type='submit']//following-sibling::input
        ```

#### parent

* Cada elemento y atributo tiene un padre.

        ```xpath
        //*[@id='rt-característica']//parent::div
        ```

#### self

    ```xpath
    =//*[@type='contraseña']//self::input
    ```

#### descendant

* Los hijos de un nodo, los hijos de los hijos, etc.

        ```xpath
        //*[@id='rt-feature']//descendant::a
        ```
