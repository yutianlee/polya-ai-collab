# Addendum: Exact-D20 Clean-Room Report Byte Hygiene

Status: **TYPOGRAPHY-ONLY ADDENDUM / ORIGINAL REPORT IMMUTABLE**.

The original report
rounds/polya-main/round_021/reviews/exact-d20-closure-clean-room.md
was reauthenticated before this addendum was created.  Its exact SHA-256 is

~~~
0ac01840b4f97ae759c47047372d6f20dda0d0c5fa4dfe3ac559d21bb16e9acc
~~~

and its length is 21,152 bytes.  The original was not edited.  Its two
accidental form-feed bytes were reproduced at zero-based offsets 4,379 and
15,972; both are byte 0x0C.  A full line-by-line TeX inspection found no
typography-only defect beyond the exact corrections enumerated below.

This was a post-verdict hygiene inspection of the immutable original report
only.  I did not read A4 material or any artifact excluded by the original
clean-room boundary.  This addendum is the only file created by the
follow-up.

## Exact textual correction ledger

Line numbers and byte offsets refer to the immutable original.

1. At line 122 and zero-based byte offset 4,379, replace the byte sequence
   0x0C followed by the ASCII text rac{576}{4} with the ASCII text
   \frac{576}{4}.  Equivalently, the malformed fragment
   >\x0Crac{576}{4} is intended to be >\frac{576}{4}.

2. At line 306, replace the fragment
   ,quad0\leq\tau<1 with ,\qquad 0\leq\tau<1.

3. At line 493, replace ,qquad R<\overline R with
   ,\qquad R<\overline R.

4. At line 497, replace ,qquad J+1>\mu-\frac12 with
   ,\qquad J+1>\mu-\frac12.

5. At line 558, replace ,qquad K\geq200 with
   ,\qquad K\geq200.

6. At line 603, replace >0,qquad with >0,\qquad.

7. At line 640 and zero-based byte offset 15,972, replace the byte sequence
   0x0C followed by the ASCII text rac b2 with the ASCII text \frac b2.
   Equivalently, the malformed fragment \x0Crac b2 is intended to be
   \frac b2.

8. At line 709, remove the redundant inner brace pair by replacing
   \frac{\rho b}{{2S}} with \frac{\rho b}{2S}.

Items 1 and 7 remove the only two forbidden control bytes in the original.
Items 2--6 restore lost TeX command backslashes and, in item 2, the intended
spacing before 0.  Item 8 is brace hygiene only.

## Corrected displays

With correction 1, the exact lower bound for the staircase guard reads

$$
k_{11}(\rho)^2=z_\rho^2+132
>\frac{49}{4}+132=\frac{577}{4}>\frac{576}{4}=12^2.
$$

With correction 2, the low-tail decomposition reads

$$
\mu-\frac12=J+\tau,
\qquad J\in\mathbb N_0,\qquad 0\leq\tau<1.
$$

With corrections 3--4, the discrete-to-continuous reserve comparisons read

$$
R\geq\mu-\frac12,\qquad R<\overline R,
$$

$$
J>\mu-\frac32,\qquad J+1>\mu-\frac12.
\tag{25}
$$

With correction 5, the universal rational superset reads

$$
\frac7{51}\leq\rho\leq\frac{39}{50},\qquad K\geq200.
\tag{32}
$$

With correction 6, the positivity and square-root guards read

$$
b=\frac{2\pi\rho}{1-\rho}>0,\qquad
S^2=\overline R^2+bK>\overline R^2.
$$

With correction 7, the first derivative of the interface integral reads

$$
I_K=\rho P+\frac b2
\operatorname{arsinh}\left(\frac{\overline R}{\sqrt{bK}}\right).
\tag{37}
$$

With correction 8, the universal curvature chain reads

$$
I_{KK}
<\frac{\rho b}{2S}+\frac{\rho b}{4S}
=\frac{3\rho b}{4S}
<\frac{3b}{4K}
\leq\frac{3b}{800}.
\tag{42}
$$

## Verdict and byte-hygiene confirmation

These corrections are exclusively typographical.  They change no
definition, inequality direction, quantifier, premise, mathematical
argument, or face assignment.  The original verdict remains exactly:
**PASS, conditional on A4 certificate validation. First issue: none.**
All mathematical reasoning in the original report is unchanged.

The addendum itself contains no forbidden C0 control byte: its only bytes in
the range 0x00--0x1F are LF line separators (0x0A).  In particular, it has
no 0x0C byte, no tab, no carriage return, no byte-order mark, and no
replacement character.
