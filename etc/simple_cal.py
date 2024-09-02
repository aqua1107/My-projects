{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "b743970b-897b-4741-a044-7ad02317e3dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Simple_Calculator:\n",
    "    def __init__(self, x, y):\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "    def add(self):\n",
    "        return self.x + self.y\n",
    "    def subtract(self):\n",
    "        return self.x - self.y\n",
    "    def multiply(self):\n",
    "        return self.x * self.y\n",
    "    def division(self):\n",
    "        try: \n",
    "            return self.x / self.y\n",
    "        except:\n",
    "            return \"Invalid\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "7352e450-50e6-4133-979f-a020d1329bc5",
   "metadata": {},
   "outputs": [],
   "source": [
    "c = Simple_Calculator(4, 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "599caae5-0843-4cda-873f-f82278b8d0b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "4\n",
      "0\n",
      "Invalid\n"
     ]
    }
   ],
   "source": [
    "print(c.add())\n",
    "print(c.subtract())\n",
    "print(c.multiply())\n",
    "print(c.division())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "f10880fb-746a-4aa9-a4e5-f31d2fea51ce",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "7a098418-3914-4f54-812b-663fe9a47b72",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
