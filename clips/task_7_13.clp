
(deffacts input-data
    (hardness 8.5)
    (density 3.72)
    (color green))

(defrule chrysoberyl
    (hardness 8.5)
    (density 3.72)
    (color yellow|brown|green)
    =>
    (assert (result chrysoberyl))
    (printout t "Chrysoberyl" crlf))

(defrule not-chrysoberyl
    (hardness ?h)
    (density ?d)
    (color ?c)
    (test (or (<> ?h 8.5)
              (<> ?d 3.72)
              (and (neq ?c yellow)
                   (neq ?c brown)
                   (neq ?c green))))
    =>
    (assert (result not-chrysoberyl))
    (printout t "Not chrysoberyl" crlf))
