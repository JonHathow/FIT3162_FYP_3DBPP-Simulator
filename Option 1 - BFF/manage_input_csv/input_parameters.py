class InputBinParameters:

    def __init__(self,
                 qty: int, width: int, height: int, depth: int, max_weight: int) -> None:
        """
        A class to sensibly store the various parameters necessary to generate desired bins of certain specified values.

        qty         - quantity of this type of bin
        width       - self-explanatory
        height      - self-explanatory
        depth       - self-explanatory

        max_weight  - maximum weight capacity of bin

        TODO:       Allow users to specify whether bin is "general" or "open-top".
        """

        self.qty:           int = qty
        self.width:         int = width
        self.height:        int = height
        self.depth:         int = depth
        self.max_weight:    int = max_weight

    def __str__(self) -> str:
        return (f"\nwidth: {self.width}"
                + f"\nheight: {self.height}"
                + f"\ndepth: {self.depth}"
                + f"\nmax_weight: {self.max_weight}"
                + f"\n")


class InputBoxParameters:

    def __init__(self, 
                 types: int, qty_lo: int, qty_hi: int, 
                 dim_lo: int, dim_hi: int, wgt_lo: int, wgt_hi: int, 
                 level_var: bool, updown_var: bool, updown: bool) -> None:
        """
        A class to sensibly store the various parameters necessary to generate desired box values.

        types           - number of box types, boxes of the same type have identical dimensions and weight
        qty_lo          - lower bound of quantity for any particular type of box
        qty_hi          - upper bound of quantity for any particular tpe of box

        TODO:           Allow users to specify lower/upper bounds for each dimension.
        dim_lo          - lower bound of dimensions (width, height, depth)
        dim_hi          - upper bound of dimensions (width, height, depth)
        wgt_lo          - lower bound of weight
        wgt_hi          - upper bound of weight

                        See main.py for a thorough explanation of the relevance of the following attributes.
        TODO:           Allow users to specify variation of loadbearing priority.
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

        self.level_var:     bool    = level_var
        self.loadbear_var:  bool    = False
        self.updown_var:    bool    = updown_var
        self.updown:        bool    = updown

    def __str__(self) -> str:
        return (f"\ntypes: {self.types}"
                + f"\nqty_lo: {self.qty_lo}, qty_hi: {self.qty_hi}"
                + f"\ndim_lo: {self.dim_lo}, dim_hi: {self.dim_hi}"
                + f"\nwgt_lo: {self.wgt_lo}, wgt_hi: {self.wgt_hi}"
                + f"\nlevel_var: {self.level_var}"
                + f"\nupdown_var: {self.updown_var}"
                + f"\nupdown: {self.updown}"
                + f"\n")