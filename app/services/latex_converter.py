from sympy.parsing.latex import parse_latex
from sympy import latex, pretty
import traceback

def convert_latex_to_sympy(latex_expr: str) -> str:
    """
    Convert LaTeX expression to SymPy format string
    """
    try:
        # Clean the input
        latex_expr = latex_expr.strip()
        
        # Parse LaTeX to SymPy expression
        sympy_expr = parse_latex(latex_expr)
        
        # Convert to string representation
        return str(sympy_expr)
        
    except ImportError as e:
        raise ValueError(f"Missing required package: {str(e)}")
    except Exception as e:
        raise ValueError(f"Failed to parse LaTeX expression '{latex_expr}': {str(e)}")