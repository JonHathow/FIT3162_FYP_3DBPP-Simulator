""" Classes to instantiate objects that store user inputs for further processing. """
# TODO: Specify units of measurement where relevant.

class InputBinParameters:
    """
    A class to store user inputs related to bins, which will be used to specify
    the dimensions of said bin(s). If there are multiple bins present, they
    will have identical dimensions and capacity.
    """

    def __init__(self, qty: int,
                 width: int, height: int, depth: int, capacity: int) -> None:
        """
        qty         - quantity of this type of bin
        width       - self-explanatory
        height      - self-explanatory
        depth       - self-explanatory
        capacity    - maximum weight capacity of bin

        TODO:       Allow users to specify whether Option 1 bins are "general" or "open-top"?
        """

        self.qty:           int = qty
        self.width:         int = width
        self.height:        int = height
        self.depth:         int = depth
        self.capacity:      int = capacity

    def __str__(self) -> str:
        return (f"\nqty: {self.qty}"
                + f"\nwidth: {self.width}"
                + f"\nheight: {self.height}"
                + f"\ndepth: {self.depth}"
                + f"\ncapacity: {self.capacity}"
                + f"\n")
    
class InputBoxParameters:
    """ 
    A class to store user inputs related to boxes, which will be used to
    generate random values for various attributes in the ranges specified.
    """

    def __init__(self, 
                 types: int, qty_lo: int, qty_hi: int, 
                 dim_lo: int, dim_hi: int, wgt_lo: int, wgt_hi: int) -> None:
        """
        types           - number of box types, boxes of the same type have identical dimensions and weight
        qty_lo          - lower bound of quantity for any particular type of box
        qty_hi          - upper bound of quantity for any particular type of box

        TODO:           Allow users to specify lower/upper bounds for each dimension?
        dim_lo          - lower bound of dimensions (width, height, depth)
        dim_hi          - upper bound of dimensions (width, height, depth)
        wgt_lo          - lower bound of weight
        wgt_hi          - upper bound of weight

        See main.py for a thorough explanation of the following attributes.
        TODO:           Allow users to specify variation of loadbearing priority?

        level_var       - different box types will have different loading priority levels if True, will default to 1 otherwise
        loadbear_var    - no variation for the time being, loadbearing priority defaults to 100 for all boxes
        updown_var      - some box types may be loaded upside down while others may not if True
        updown          - relevant only if updown_var is False, specifies whether boxes can be loaded upside down or not
        """

        self.types:         int     = types
        self.qty_lo:        int     = qty_lo
        self.qty_hi:        int     = qty_hi

        self.dim_lo:        int     = dim_lo
        self.dim_hi:        int     = dim_hi
        self.wgt_lo:        int     = wgt_lo
        self.wgt_hi:        int     = wgt_hi

        self.level_var:     bool    = False
        self.loadbear_var:  bool    = False
        self.updown_var:    bool    = False
        self.updown:        bool    = False

    def set_option1_params(self, level_var: bool, updown_var: bool, updown: bool) -> None:
        """ Set values of attributes relevant only to boxes in Option 1. """
        self.level_var  = level_var
        self.updown_var = updown_var
        self.updown     = updown

    def __str__(self) -> str:
        return (f"\ntypes: {self.types}"
                + f"\nqty_lo: {self.qty_lo}, qty_hi: {self.qty_hi}"
                + f"\ndim_lo: {self.dim_lo}, dim_hi: {self.dim_hi}"
                + f"\nwgt_lo: {self.wgt_lo}, wgt_hi: {self.wgt_hi}"
                + f"\nlevel_var: {self.level_var}"
                + f"\nloadbear_var: {self.loadbear_var}"
                + f"\nupdown_var: {self.updown_var}"
                + f"\nupdown: {self.updown}"
                + f"\n")