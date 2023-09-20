class ParkingEntry(db.Model):
    __tablename__ = 'parking'

    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(10), nullable=False)
    entry_time = db.Column(db.TIMESTAMP(timezone=True), default=db.func.now())
    exit_time = db.Column(db.TIMESTAMP(timezone=True))
    paid = db.Column(db.Boolean, default=False)

    def __init__(self, plate):
        self.plate = plate
