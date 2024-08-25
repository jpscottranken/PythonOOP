import constants as c
import employee  as emp

class PieceWorker(emp.Employee):
  def __init__(self, empNumber, firstName, lastName, numberOfPieces, pricePerPiece):
    super().__init__(empNumber, firstName, lastName)

    # Range check on number of pieces
    if not (c.MINPIECES <= numberOfPieces <= c.MAXPIECES):
      raise ValueError(f"Number Of Pieces Must Be Between {c.MINPIECES} and {c.MAXPIECES}.")
    
    # Range check on price per piece
    if not (c.MINPPIECE <= pricePerPiece <= c.MAXPPIECE):
      raise ValueError(f"Price Per Piece Must Be Between {c.MINPPIECE} and {c.MAXPPIECE}.")
    
    self.numberOfPieces  = numberOfPieces
    self.pricePerPiece   = pricePerPiece

  def calculateGrossPay(self):
    self.grossPay = self.numberOfPieces * self.pricePerPiece
    
    return self.grossPay
