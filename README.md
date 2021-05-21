<img src='https://drive.google.com/uc?id=1lmhgAs5rStRgqPMjllarksSBsmum7Ag5'>


# colorsaur
 The class implements very simple gradients using the RGB space and some simple linear algebra.

 # basic math
 A color can be expressed as a vector in a 3D $(r,g,b)$ space where $r,g,b \in [0,255]$ are integer numbers.

In order to find the possible colors that fall between a pair $[\bar{c_1}=(r_1,g_1,b_1),\bar{c_2}=(r_2,g_2,b_2)]$ we need to find the line connecting $\bar{c_1}$ and $\bar{c_2}$. In this case we will have a 'simple' linear gradient.

First of all we compute the 'director vector' which gives the direction of this line. This is easily the difference between $\bar{c_1}$ and $\bar{c_2}$. $\bar{v_d}=\bar{c_1}-\bar{c_2}$.

If we now multiply $\bar{v_d}$ by a parameter $t$ we find the parametric equation of the line in the direction connecting $\bar{c_1}$ and $\bar{c_2}$: $\bar{c_0}=\bar{v_d}t$. This line however passed through the origin, and we have to shift it to let it pass through $\bar{c_1}$.

The desired equation is therefore:
 $\bar{c}=\bar{v_d}t+\bar{c_1}$

Note that:
 $t=0 \Rightarrow \bar{c}=\bar{c_1}$
 $t=-1 \Rightarrow \bar{c}=\bar{c_2}$

 So that if we want to find the gradient colors we have to vary $t$ in the range $[-1,0]$

 # usage

 Gradient_2c()
 class: inizialized by giving as input 2 color in hex format.

.pick_color(index)
mehod: pick up a color in the gradient. Here 'index' is a value between $[-1,0]$. Return a tuple in (r,g,b) format.

.get_gradient(depth)
mehod: You can pick up the entire gradient. The method returns an array of (r,g,b) tuples of length equal to the 'depht' parameter.
