definitions = {
	'polimorfizm':"In programming languages and type theory, polymorphism is the\n provision of a single interface to entities of different    \n types or the use of a single symbol to represent multiple\n different types",
	'skalowalnosc':"ability to change performance and number of virtual mashine \nin use",
	'interpreter':"computer program that interprets code line by line",
	'compiler':"computer program that compiles entire code as long as it has no \n errors",
	'enkapsulacja':"refers to the bundling of data with the methods that operate\n on that data, or the restricting of direct access to some of\n an object's components.[1] Encapsulation is used to hide the\n values or state of a structured data object inside a class, \n preventing unauthorized parties' direct access to them.     \n Publicly accessible methods are generally provided in the   \n class  to access the     \n values, and other client classes call these methods to     \n retrieve and modify the values within the object."
}

for definition, description in definitions.items():
	print(f"{definition.upper()} \n\n")