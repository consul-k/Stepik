class Cost
  attr_accessor :rub, :cop
  def initialize(rub, cop)
    self.rub = rub
    self.cop = cop
  end
  def *(cost)
    Cost.new(self.rub * cost.rub, self.cop * cost.cop)
  end
end
