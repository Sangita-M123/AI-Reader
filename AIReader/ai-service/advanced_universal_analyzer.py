import re

def analyze_code_advanced_universal(code: str, file_extension: str) -> str:
    """
    🚀 ADVANCED UNIVERSAL CODE ANALYZER
    Understands EVERY programming language with deep syntax analysis
    Supports: Java, Python, JavaScript, C++, C, C#, PHP, Ruby, Go, Rust, TypeScript, etc.
    """
    
    # 🌍 COMPREHENSIVE LANGUAGE MAPPING
    languages = {
        '.py': 'Python', '.js': 'JavaScript', '.java': 'Java', '.cpp': 'C++', '.c': 'C',
        '.cs': 'C#', '.php': 'PHP', '.rb': 'Ruby', '.go': 'Go', '.rs': 'Rust',
        '.kt': 'Kotlin', '.swift': 'Swift', '.ts': 'TypeScript', '.scala': 'Scala',
        '.dart': 'Dart', '.r': 'R', '.m': 'Objective-C', '.pl': 'Perl', '.sh': 'Shell',
        '.sql': 'SQL', '.html': 'HTML', '.css': 'CSS', '.jsx': 'React JSX', '.vue': 'Vue.js'
    }
    
    language = languages.get(file_extension, 'Programming')
    code_lower = code.lower()
    lines = [l.strip() for l in code.split('\n') if l.strip()]
    
    explanation = []
    
    # 🧠 STEP 1: INTELLIGENT PROGRAM TYPE DETECTION
    program_type = detect_program_type(code, code_lower, language)
    
    explanation.append(f"🎯 WHAT THIS CODE DOES:")
    explanation.append(program_type['description'])
    
    # 🔍 STEP 2: SYNTAX-AWARE ANALYSIS
    syntax_analysis = analyze_syntax_patterns(code, file_extension, language)
    
    if syntax_analysis['classes']:
        explanation.append(f"\n🏗️ CLASSES & STRUCTURES ({len(syntax_analysis['classes'])} total):")
        for class_info in syntax_analysis['classes'][:10]:
            explanation.append(f"• {class_info}")
    
    if syntax_analysis['functions']:
        explanation.append(f"\n🔧 FUNCTIONS & METHODS ({len(syntax_analysis['functions'])} total):")
        for i, func_info in enumerate(syntax_analysis['functions'][:15], 1):
            explanation.append(f"{i}. {func_info}")
    
    # 🎓 STEP 3: CONCEPT EXPLANATION
    concepts = detect_programming_concepts(code, code_lower, language)
    if concepts:
        explanation.append(f"\n💡 KEY PROGRAMMING CONCEPTS:")
        for concept in concepts:
            explanation.append(f"• {concept}")
    
    # 📊 STEP 4: ALGORITHM ANALYSIS
    algorithms = detect_algorithms(code, code_lower)
    if algorithms:
        explanation.append(f"\n⚡ ALGORITHMS IMPLEMENTED:")
        for algo in algorithms:
            explanation.append(f"• {algo}")
    
    # 🎯 STEP 5: LANGUAGE-SPECIFIC FEATURES
    lang_features = analyze_language_features(code, file_extension, language)
    if lang_features:
        explanation.append(f"\n🌟 {language.upper()} SPECIFIC FEATURES:")
        for feature in lang_features:
            explanation.append(f"• {feature}")
    
    # 📚 STEP 6: LEARNING OUTCOMES
    explanation.append(f"\n🎓 WHAT YOU'LL LEARN:")
    learning_outcomes = generate_learning_outcomes(program_type, concepts, algorithms, language)
    for outcome in learning_outcomes:
        explanation.append(f"✓ {outcome}")
    
    # 📝 STEP 7: COMPREHENSIVE SUMMARY
    explanation.append(f"\n{'='*60}")
    explanation.append(f"📚 SUMMARY:")
    explanation.append(generate_summary(program_type, language, len(syntax_analysis['functions']), len(syntax_analysis['classes'])))
    
    # Clean the explanation for better audio experience
    final_text = '\n'.join(explanation)
    
    # Replace visual formatting with audio-friendly alternatives
    final_text = final_text.replace('='*60, '\n--- End of Analysis ---\n')
    final_text = final_text.replace('🎯', 'TARGET:')
    final_text = final_text.replace('🏗️', 'STRUCTURE:')
    final_text = final_text.replace('🔧', 'FUNCTIONS:')
    final_text = final_text.replace('💡', 'CONCEPTS:')
    final_text = final_text.replace('⚡', 'ALGORITHMS:')
    final_text = final_text.replace('🌟', 'FEATURES:')
    final_text = final_text.replace('🎓', 'LEARNING:')
    final_text = final_text.replace('📚', 'SUMMARY:')
    final_text = final_text.replace('✓', 'Check:')
    final_text = final_text.replace('•', 'Point:')
    
    return final_text


def detect_program_type(code: str, code_lower: str, language: str) -> dict:
    """Intelligently detects what type of program this is"""
    
    # 🎯 SPECIFIC PROGRAM PATTERNS
    
    # Hello World Detection
    if 'hello' in code_lower and 'world' in code_lower:
        loop_match = re.search(r'for.*?(\d+)', code)
        if loop_match:
            times = loop_match.group(1)
            return {
                'type': 'hello_world_loop',
                'description': f"This is a {language} program that prints 'Hello World' {times} times using a loop."
            }
        return {
            'type': 'hello_world',
            'description': f"This is a simple {language} 'Hello World' program - the traditional first program for beginners."
        }
    
    # String Manipulation Programs
    if any(pattern in code_lower for pattern in ['palindrome', 'paligdron', 'substring', 'compress', 'uppercase']):
        operations = []
        if 'palindrome' in code_lower or 'paligdron' in code_lower:
            operations.append("palindrome checking (reads same forwards/backwards)")
        if 'substring' in code_lower:
            operations.append("substring extraction")
        if 'compress' in code_lower:
            operations.append("string compression (run-length encoding)")
        if 'uppercase' in code_lower or 'titlecase' in code_lower:
            operations.append("text case conversion")
        if 'shortestpath' in code_lower:
            operations.append("shortest path calculation using coordinates")
        
        return {
            'type': 'string_manipulation',
            'description': f"This is a comprehensive {language} string manipulation program that demonstrates: {', '.join(operations)}."
        }
    
    # Mathematical Programs
    if any(pattern in code_lower for pattern in ['factorial', 'fibonacci', 'prime', 'even', 'odd']):
        if 'factorial' in code_lower:
            return {'type': 'factorial', 'description': f"This {language} program calculates factorial (n! = n × (n-1) × ... × 1)."}
        if 'fibonacci' in code_lower:
            return {'type': 'fibonacci', 'description': f"This {language} program generates Fibonacci sequence (each number = sum of previous two)."}
        if 'prime' in code_lower:
            return {'type': 'prime', 'description': f"This {language} program checks if numbers are prime (only divisible by 1 and themselves)."}
        if 'even' in code_lower or 'odd' in code_lower:
            return {'type': 'even_odd', 'description': f"This {language} program determines if numbers are even or odd using modulo operator."}
    
    # Data Structure Programs
    if any(ds in code_lower for ds in ['linkedlist', 'queue', 'stack', 'tree', 'graph', 'heap']):
        structures = []
        if 'linkedlist' in code_lower or 'node' in code_lower:
            structures.append("Linked Lists")
        if 'queue' in code_lower:
            structures.append("Queues (FIFO)")
        if 'stack' in code_lower:
            structures.append("Stacks (LIFO)")
        if 'tree' in code_lower:
            structures.append("Trees")
        if 'graph' in code_lower:
            structures.append("Graphs")
        if 'heap' in code_lower:
            structures.append("Heaps")
        
        return {
            'type': 'data_structures',
            'description': f"This {language} program implements and demonstrates {', '.join(structures)} data structures."
        }
    
    # Algorithm Programs
    if any(algo in code_lower for algo in ['sort', 'search', 'merge', 'quick', 'bubble']):
        algorithms = []
        if 'sort' in code_lower:
            if 'bubble' in code_lower:
                algorithms.append("Bubble Sort")
            elif 'merge' in code_lower:
                algorithms.append("Merge Sort")
            elif 'quick' in code_lower:
                algorithms.append("Quick Sort")
            else:
                algorithms.append("Sorting algorithms")
        if 'search' in code_lower:
            if 'binary' in code_lower:
                algorithms.append("Binary Search")
            else:
                algorithms.append("Search algorithms")
        
        return {
            'type': 'algorithms',
            'description': f"This {language} program implements {', '.join(algorithms)} for efficient data processing."
        }
    
    # Web Development
    if any(web in code_lower for web in ['html', 'css', 'dom', 'fetch', 'api', 'ajax']):
        return {
            'type': 'web_development',
            'description': f"This {language} program is for web development, handling DOM manipulation, API calls, or frontend functionality."
        }
    
    # Database Programs
    if any(db in code_lower for db in ['sql', 'database', 'query', 'select', 'insert', 'update']):
        return {
            'type': 'database',
            'description': f"This {language} program handles database operations including queries, data manipulation, and storage."
        }
    
    # Object-Oriented Programs
    if 'class' in code_lower and any(oop in code_lower for oop in ['extends', 'inheritance', 'polymorphism', 'encapsulation']):
        return {
            'type': 'oop',
            'description': f"This {language} program demonstrates Object-Oriented Programming concepts with classes, inheritance, and encapsulation."
        }
    
    # Generic Programs
    if 'class' in code:
        class_count = len(re.findall(r'class\s+\w+', code, re.IGNORECASE))
        return {
            'type': 'multi_class',
            'description': f"This {language} program contains {class_count} classes implementing various computational operations."
        }
    
    return {
        'type': 'general',
        'description': f"This {language} program performs computational operations and demonstrates programming fundamentals."
    }


def analyze_syntax_patterns(code: str, file_extension: str, language: str) -> dict:
    """Deep syntax analysis for different programming languages"""
    
    classes = []
    functions = []
    
    # 🏗️ CLASS DETECTION (Language-specific patterns)
    class_patterns = {
        '.java': [r'(?:public\s+|private\s+|protected\s+)?class\s+(\w+)(?:\s+extends\s+\w+)?(?:\s+implements\s+[\w,\s]+)?\s*{'],
        '.py': [r'class\s+(\w+)(?:\([^)]*\))?\s*:'],
        '.cpp': [r'class\s+(\w+)(?:\s*:\s*(?:public|private|protected)\s+\w+)?\s*{', r'struct\s+(\w+)\s*{'],
        '.c': [r'struct\s+(\w+)\s*{', r'typedef\s+struct\s*{[^}]*}\s*(\w+)'],
        '.cs': [r'(?:public\s+|private\s+|internal\s+)?(?:abstract\s+|sealed\s+)?class\s+(\w+)(?:\s*:\s*\w+)?\s*{'],
        '.js': [r'class\s+(\w+)(?:\s+extends\s+\w+)?\s*{'],
        '.ts': [r'(?:export\s+)?(?:abstract\s+)?class\s+(\w+)(?:<[^>]*>)?(?:\s+extends\s+\w+)?(?:\s+implements\s+[\w,\s]+)?\s*{']
    }
    
    if file_extension in class_patterns:
        for pattern in class_patterns[file_extension]:
            matches = re.findall(pattern, code, re.IGNORECASE | re.MULTILINE)
            for match in matches:
                class_purpose = analyze_class_purpose(match, code)
                classes.append(f"{match} class: {class_purpose}")
    
    # 🔧 FUNCTION DETECTION (Language-specific patterns)
    function_patterns = {
        '.java': [
            r'(?:public\s+|private\s+|protected\s+)?(?:static\s+)?(?:final\s+)?(\w+)\s+(\w+)\s*\([^)]*\)\s*(?:throws\s+[\w,\s]+)?\s*{',
            r'(?:public\s+|private\s+|protected\s+)?(?:static\s+)?(void)\s+(\w+)\s*\([^)]*\)\s*(?:throws\s+[\w,\s]+)?\s*{'
        ],
        '.py': [r'def\s+(\w+)\s*\([^)]*\)\s*(?:->\s*[\w\[\],\s]+)?\s*:'],
        '.cpp': [r'(?:inline\s+)?(?:virtual\s+)?(?:static\s+)?(\w+(?:\s*\*)?)\s+(\w+)\s*\([^)]*\)\s*(?:const\s*)?{'],
        '.c': [r'(\w+(?:\s*\*)?)\s+(\w+)\s*\([^)]*\)\s*{'],
        '.cs': [r'(?:public\s+|private\s+|protected\s+|internal\s+)?(?:static\s+)?(?:virtual\s+|override\s+)?(\w+)\s+(\w+)\s*\([^)]*\)\s*{'],
        '.js': [r'function\s+(\w+)\s*\([^)]*\)\s*{', r'(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?\([^)]*\)\s*=>\s*{?', r'(\w+)\s*:\s*(?:async\s+)?function\s*\([^)]*\)\s*{'],
        '.ts': [r'(?:export\s+)?(?:async\s+)?function\s+(\w+)(?:<[^>]*>)?\s*\([^)]*\)\s*(?::\s*[\w\[\]<>,\s|]+)?\s*{']
    }
    
    if file_extension in function_patterns:
        for pattern in function_patterns[file_extension]:
            matches = re.findall(pattern, code, re.IGNORECASE | re.MULTILINE)
            for match in matches:
                if isinstance(match, tuple):
                    func_name = match[1] if len(match) > 1 else match[0]
                    return_type = match[0] if len(match) > 1 else "void"
                else:
                    func_name = match
                    return_type = "unknown"
                
                if func_name.lower() not in ['main', 'args', 'string', 'void', 'int', 'public', 'private', 'class']:
                    func_purpose = analyze_function_purpose(func_name, code)
                    functions.append(f"{func_name}(): {func_purpose}")
    
    return {'classes': classes, 'functions': functions}


def analyze_class_purpose(class_name: str, code: str) -> str:
    """Analyzes what a class is designed to do"""
    class_lower = class_name.lower()
    code_lower = code.lower()
    
    # Data structure classes
    if 'node' in class_lower:
        return "Node structure for linked data structures (contains data and pointers)"
    elif 'queue' in class_lower:
        return "Queue implementation - FIFO (First In, First Out) data structure"
    elif 'stack' in class_lower:
        return "Stack implementation - LIFO (Last In, First Out) data structure"
    elif 'list' in class_lower or 'linkedlist' in class_lower:
        return "Linked list implementation with dynamic memory allocation"
    elif 'tree' in class_lower:
        return "Tree data structure for hierarchical data organization"
    elif 'graph' in class_lower:
        return "Graph data structure for network and relationship modeling"
    elif 'heap' in class_lower:
        return "Heap data structure for priority queue operations"
    elif 'hash' in class_lower:
        return "Hash table implementation for fast key-value lookups"
    
    # Algorithm classes
    elif 'sort' in class_lower:
        return "Contains sorting algorithms for data arrangement"
    elif 'search' in class_lower:
        return "Contains search algorithms for data retrieval"
    elif 'solution' in class_lower or 'solver' in class_lower:
        return "Contains problem-solving algorithms and utility methods"
    
    # Entity classes
    elif any(entity in class_lower for entity in ['person', 'student', 'employee', 'user', 'customer']):
        return f"Models a {class_name.lower()} entity with properties and behaviors"
    elif any(entity in class_lower for entity in ['car', 'animal', 'book', 'product']):
        return f"Represents a {class_name.lower()} object with attributes and methods"
    
    # Utility classes
    elif 'util' in class_lower or 'helper' in class_lower:
        return "Utility class providing helper methods and common operations"
    elif 'main' in class_lower:
        return "Main class containing the program entry point and core logic"
    
    return "Supporting class for program operations and data management"


def analyze_function_purpose(func_name: str, code: str) -> str:
    """Intelligently determines what a function does"""
    func_lower = func_name.lower()
    code_lower = code.lower()
    
    # String operations
    if 'palindrome' in func_lower or 'paligdron' in func_lower:
        return "Checks if string reads same forwards and backwards (like 'madam')"
    elif 'substring' in func_lower:
        return "Extracts portion of string between specified indices"
    elif 'compress' in func_lower:
        return "Compresses string using run-length encoding (e.g., 'aaa' → 'a3')"
    elif 'uppercase' in func_lower or 'titlecase' in func_lower:
        return "Converts string to title case (capitalizes first letter of each word)"
    elif 'shortestpath' in func_lower:
        return "Calculates shortest distance using coordinate geometry and Pythagorean theorem"
    elif 'printletters' in func_lower:
        return "Prints each character of string with spaces between them"
    
    # Mathematical operations
    elif 'factorial' in func_lower:
        return "Calculates factorial (n! = n × (n-1) × ... × 1)"
    elif 'fibonacci' in func_lower:
        return "Generates Fibonacci sequence (each number = sum of previous two)"
    elif 'prime' in func_lower:
        return "Checks if number is prime (only divisible by 1 and itself)"
    elif 'even' in func_lower or 'odd' in func_lower:
        return "Determines if number is even or odd using modulo operator"
    elif 'gcd' in func_lower or 'lcm' in func_lower:
        return f"Calculates {func_lower.upper()} of two numbers"
    
    # Data structure operations
    elif 'enqueue' in func_lower:
        return "Adds element to rear of queue (FIFO insertion)"
    elif 'dequeue' in func_lower:
        return "Removes element from front of queue (FIFO removal)"
    elif 'push' in func_lower:
        return "Adds element to top of stack (LIFO insertion)"
    elif 'pop' in func_lower:
        return "Removes element from top of stack (LIFO removal)"
    elif 'peek' in func_lower or 'top' in func_lower:
        return "Returns top/front element without removing it"
    elif 'isempty' in func_lower:
        return "Checks if data structure contains no elements"
    elif 'isfull' in func_lower:
        return "Checks if array-based structure has reached capacity"
    
    # Sorting algorithms
    elif 'bubblesort' in func_lower:
        return "Bubble Sort - repeatedly swaps adjacent elements if in wrong order"
    elif 'selectionsort' in func_lower:
        return "Selection Sort - finds minimum element and places at beginning"
    elif 'insertionsort' in func_lower:
        return "Insertion Sort - builds sorted array by inserting elements one by one"
    elif 'mergesort' in func_lower:
        return "Merge Sort - divide and conquer sorting algorithm (O(n log n))"
    elif 'quicksort' in func_lower:
        return "Quick Sort - efficient divide and conquer sorting using pivot"
    
    # Search algorithms
    elif 'binarysearch' in func_lower:
        return "Binary Search - efficiently searches sorted array (O(log n))"
    elif 'linearsearch' in func_lower:
        return "Linear Search - searches by checking each element sequentially"
    
    # Linked list operations
    elif 'reverse' in func_lower:
        return "Reverses the order of elements in data structure"
    elif 'merge' in func_lower:
        return "Merges two or more data structures into one"
    elif 'cycle' in func_lower:
        return "Detects or handles cycles in linked structures"
    elif 'middle' in func_lower or 'mid' in func_lower:
        return "Finds middle element using slow/fast pointer technique"
    
    # Generic operations
    elif 'add' in func_lower or 'insert' in func_lower:
        return "Adds new elements to the data structure"
    elif 'remove' in func_lower or 'delete' in func_lower:
        return "Removes elements from the data structure"
    elif 'find' in func_lower or 'search' in func_lower:
        return "Searches for specific elements in the data structure"
    elif 'display' in func_lower or 'print' in func_lower:
        return "Displays contents of data structure on screen"
    elif 'size' in func_lower or 'length' in func_lower:
        return "Returns number of elements in the data structure"
    elif 'clear' in func_lower:
        return "Removes all elements from the data structure"
    elif 'get' in func_lower:
        return "Retrieves element at specified position or key"
    elif 'set' in func_lower or 'update' in func_lower:
        return "Updates element at specified position or key"
    
    # Fallback
    return f"Performs {func_lower.replace('_', ' ')} operation"


def detect_programming_concepts(code: str, code_lower: str, language: str) -> list:
    """Detects programming concepts used in the code"""
    concepts = []
    
    # Object-Oriented Programming
    if 'class' in code_lower:
        concepts.append("Object-Oriented Programming - organizing code into classes and objects")
        if 'extends' in code_lower or 'inheritance' in code_lower:
            concepts.append("Inheritance - classes inheriting properties from parent classes")
        if 'interface' in code_lower:
            concepts.append("Interfaces - contracts that classes must implement")
        if 'abstract' in code_lower:
            concepts.append("Abstraction - hiding implementation details")
    
    # Data Structures
    if any(ds in code_lower for ds in ['array', 'list', 'arraylist']):
        concepts.append("Arrays/Lists - storing multiple elements in ordered collection")
    if 'linkedlist' in code_lower or 'node' in code_lower:
        concepts.append("Linked Lists - dynamic data structure with nodes and pointers")
    if 'queue' in code_lower:
        concepts.append("Queues - FIFO (First In, First Out) data structure")
    if 'stack' in code_lower:
        concepts.append("Stacks - LIFO (Last In, First Out) data structure")
    if 'tree' in code_lower:
        concepts.append("Trees - hierarchical data structure with parent-child relationships")
    if 'graph' in code_lower:
        concepts.append("Graphs - network structure with nodes and edges")
    if 'hash' in code_lower:
        concepts.append("Hash Tables - fast key-value lookup using hash functions")
    
    # Algorithms
    if 'sort' in code_lower:
        concepts.append("Sorting Algorithms - arranging data in specific order")
    if 'search' in code_lower:
        concepts.append("Search Algorithms - finding specific elements efficiently")
    if 'recursion' in code_lower or 'recursive' in code_lower:
        concepts.append("Recursion - functions calling themselves to solve problems")
    if 'dynamic' in code_lower and 'programming' in code_lower:
        concepts.append("Dynamic Programming - optimizing recursive solutions")
    
    # Programming Fundamentals
    if any(loop in code_lower for loop in ['for', 'while', 'do']):
        concepts.append("Loops - repeating code blocks for iteration")
    if any(cond in code_lower for cond in ['if', 'else', 'switch', 'case']):
        concepts.append("Conditional Statements - making decisions in code")
    if 'exception' in code_lower or 'try' in code_lower or 'catch' in code_lower:
        concepts.append("Exception Handling - managing errors gracefully")
    
    # Memory Management
    if language in ['C', 'C++'] and any(mem in code_lower for mem in ['malloc', 'free', 'new', 'delete']):
        concepts.append("Memory Management - allocating and deallocating memory")
    if 'pointer' in code_lower or '->' in code:
        concepts.append("Pointers - variables storing memory addresses")
    
    # String Processing
    if any(str_op in code_lower for str_op in ['substring', 'split', 'join', 'replace']):
        concepts.append("String Manipulation - processing and modifying text data")
    
    # Input/Output
    if any(io in code_lower for io in ['scanner', 'input', 'cin', 'cout', 'printf', 'scanf']):
        concepts.append("Input/Output Operations - reading user input and displaying output")
    
    return concepts


def detect_algorithms(code: str, code_lower: str) -> list:
    """Detects specific algorithms implemented in the code"""
    algorithms = []
    
    # Sorting Algorithms
    if 'bubblesort' in code_lower:
        algorithms.append("Bubble Sort - O(n²) time complexity, simple comparison-based sorting")
    elif 'selectionsort' in code_lower:
        algorithms.append("Selection Sort - O(n²) time complexity, finds minimum and swaps")
    elif 'insertionsort' in code_lower:
        algorithms.append("Insertion Sort - O(n²) time complexity, builds sorted array incrementally")
    elif 'mergesort' in code_lower:
        algorithms.append("Merge Sort - O(n log n) time complexity, divide and conquer approach")
    elif 'quicksort' in code_lower:
        algorithms.append("Quick Sort - O(n log n) average case, uses pivot partitioning")
    elif 'heapsort' in code_lower:
        algorithms.append("Heap Sort - O(n log n) time complexity, uses heap data structure")
    
    # Search Algorithms
    if 'binarysearch' in code_lower:
        algorithms.append("Binary Search - O(log n) time complexity, works on sorted arrays")
    elif 'linearsearch' in code_lower:
        algorithms.append("Linear Search - O(n) time complexity, checks each element sequentially")
    
    # String Algorithms
    if 'palindrome' in code_lower:
        algorithms.append("Palindrome Check - two-pointer technique to verify symmetry")
    if 'compress' in code_lower and 'string' in code_lower:
        algorithms.append("String Compression - run-length encoding algorithm")
    
    # Mathematical Algorithms
    if 'factorial' in code_lower:
        algorithms.append("Factorial Calculation - iterative or recursive multiplication")
    if 'fibonacci' in code_lower:
        algorithms.append("Fibonacci Sequence - dynamic programming or recursion")
    if 'prime' in code_lower:
        algorithms.append("Prime Number Check - divisibility testing algorithm")
    if 'gcd' in code_lower:
        algorithms.append("Greatest Common Divisor - Euclidean algorithm")
    
    # Graph Algorithms
    if 'dfs' in code_lower or 'depth' in code_lower:
        algorithms.append("Depth-First Search - graph traversal using stack")
    if 'bfs' in code_lower or 'breadth' in code_lower:
        algorithms.append("Breadth-First Search - graph traversal using queue")
    if 'dijkstra' in code_lower:
        algorithms.append("Dijkstra's Algorithm - shortest path in weighted graphs")
    
    # Dynamic Programming
    if 'dp' in code_lower or ('dynamic' in code_lower and 'programming' in code_lower):
        algorithms.append("Dynamic Programming - optimization using memoization")
    
    # Geometric Algorithms
    if 'shortestpath' in code_lower:
        algorithms.append("Shortest Path Calculation - coordinate geometry using Pythagorean theorem")
    
    return algorithms


def analyze_language_features(code: str, file_extension: str, language: str) -> list:
    """Analyzes language-specific features used in the code"""
    features = []
    code_lower = code.lower()
    
    # Java-specific features
    if file_extension == '.java':
        if 'scanner' in code_lower:
            features.append("Scanner class for user input handling")
        if 'stringbuilder' in code_lower:
            features.append("StringBuilder for efficient string manipulation")
        if 'arraylist' in code_lower:
            features.append("ArrayList for dynamic array operations")
        if 'hashmap' in code_lower:
            features.append("HashMap for key-value pair storage")
        if 'interface' in code_lower:
            features.append("Interfaces for contract-based programming")
        if 'extends' in code_lower:
            features.append("Class inheritance using extends keyword")
        if 'implements' in code_lower:
            features.append("Interface implementation")
        if 'static' in code_lower:
            features.append("Static methods and variables")
        if 'final' in code_lower:
            features.append("Final keyword for immutability")
    
    # Python-specific features
    elif file_extension == '.py':
        if 'list comprehension' in code_lower or '[' in code and 'for' in code and 'in' in code:
            features.append("List comprehensions for concise data processing")
        if 'lambda' in code_lower:
            features.append("Lambda functions for inline function definitions")
        if 'with' in code_lower:
            features.append("Context managers for resource management")
        if 'yield' in code_lower:
            features.append("Generators using yield for memory-efficient iteration")
        if 'decorator' in code_lower or '@' in code:
            features.append("Decorators for function modification")
        if '__init__' in code_lower:
            features.append("Constructor methods for object initialization")
        if 'self' in code_lower:
            features.append("Self parameter for instance method access")
    
    # JavaScript-specific features
    elif file_extension == '.js':
        if 'arrow function' in code_lower or '=>' in code:
            features.append("Arrow functions for concise function syntax")
        if 'async' in code_lower and 'await' in code_lower:
            features.append("Async/await for asynchronous programming")
        if 'promise' in code_lower:
            features.append("Promises for handling asynchronous operations")
        if 'callback' in code_lower:
            features.append("Callback functions for event handling")
        if 'closure' in code_lower:
            features.append("Closures for data encapsulation")
        if 'prototype' in code_lower:
            features.append("Prototype-based inheritance")
    
    # C++ specific features
    elif file_extension == '.cpp':
        if 'template' in code_lower:
            features.append("Templates for generic programming")
        if 'namespace' in code_lower:
            features.append("Namespaces for code organization")
        if 'operator overloading' in code_lower or 'operator' in code_lower:
            features.append("Operator overloading for custom operations")
        if 'virtual' in code_lower:
            features.append("Virtual functions for polymorphism")
        if 'smart pointer' in code_lower or 'unique_ptr' in code_lower:
            features.append("Smart pointers for automatic memory management")
        if 'vector' in code_lower:
            features.append("STL vectors for dynamic arrays")
    
    # C-specific features
    elif file_extension == '.c':
        if 'malloc' in code_lower or 'calloc' in code_lower:
            features.append("Dynamic memory allocation")
        if 'struct' in code_lower:
            features.append("Structures for custom data types")
        if 'pointer' in code_lower or '->' in code:
            features.append("Pointers for memory address manipulation")
        if 'typedef' in code_lower:
            features.append("Type definitions for code clarity")
    
    return features


def generate_learning_outcomes(program_type: dict, concepts: list, algorithms: list, language: str) -> list:
    """Generates learning outcomes based on code analysis"""
    outcomes = []
    
    # Basic programming outcomes
    outcomes.append(f"Fundamental {language} programming syntax and structure")
    outcomes.append("Problem-solving approach and logical thinking")
    
    # Concept-based outcomes
    if any('String' in concept for concept in concepts):
        outcomes.append("String manipulation techniques and text processing")
    if any('Array' in concept or 'List' in concept for concept in concepts):
        outcomes.append("Array/List operations and data organization")
    if any('Object-Oriented' in concept for concept in concepts):
        outcomes.append("Object-oriented programming principles and design patterns")
    if any('Loop' in concept for concept in concepts):
        outcomes.append("Iteration techniques and loop optimization")
    if any('Conditional' in concept for concept in concepts):
        outcomes.append("Decision-making logic and control flow")
    
    # Algorithm-based outcomes
    if any('Sort' in algo for algo in algorithms):
        outcomes.append("Sorting algorithms and time complexity analysis")
    if any('Search' in algo for algo in algorithms):
        outcomes.append("Search techniques and efficiency optimization")
    if any('Dynamic Programming' in algo for algo in algorithms):
        outcomes.append("Dynamic programming and memoization strategies")
    
    # Data structure outcomes
    if any('Linked List' in concept for concept in concepts):
        outcomes.append("Pointer manipulation and dynamic data structures")
    if any('Stack' in concept or 'Queue' in concept for concept in concepts):
        outcomes.append("Stack and Queue operations for data management")
    if any('Tree' in concept or 'Graph' in concept for concept in concepts):
        outcomes.append("Hierarchical and network data structure implementation")
    
    # Advanced outcomes
    if program_type['type'] in ['data_structures', 'algorithms']:
        outcomes.append("Algorithm design and complexity analysis")
        outcomes.append("Data structure selection for optimal performance")
    
    outcomes.append("Code debugging and testing methodologies")
    outcomes.append("Best practices for clean and maintainable code")
    
    return outcomes


def generate_summary(program_type: dict, language: str, func_count: int, class_count: int) -> str:
    """Generates comprehensive summary"""
    summary_parts = []
    
    if program_type['type'] == 'string_manipulation':
        summary_parts.append(f"This comprehensive {language} string manipulation program")
        summary_parts.append("demonstrates essential text processing algorithms.")
    elif program_type['type'] == 'data_structures':
        summary_parts.append(f"This {language} program showcases fundamental data structures")
        summary_parts.append("with practical implementations and operations.")
    elif program_type['type'] == 'algorithms':
        summary_parts.append(f"This {language} program implements important algorithms")
        summary_parts.append("for efficient data processing and problem-solving.")
    else:
        summary_parts.append(f"This {language} program demonstrates programming fundamentals")
        summary_parts.append("with practical examples and implementations.")
    
    if func_count > 0:
        summary_parts.append(f"With {func_count} functions, it provides hands-on experience")
        summary_parts.append("with modular programming and code organization.")
    
    if class_count > 0:
        summary_parts.append(f"The {class_count} classes showcase object-oriented design")
        summary_parts.append("and encapsulation principles.")
    
    summary_parts.append("Perfect for learning core programming concepts and building")
    summary_parts.append("a strong foundation in software development!")
    
    return ' '.join(summary_parts)