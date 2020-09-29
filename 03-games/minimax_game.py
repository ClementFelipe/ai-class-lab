{
 "metadata": {
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
   "version": "3.7.6-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "Python 3.7.6 64-bit ('xxx': conda)",
   "display_name": "Python 3.7.6 64-bit ('xxx': conda)",
   "metadata": {
    "interpreter": {
     "hash": "36f349602b5ae1f7858e11d031ce0c77385db5310f2fd6fc2b94903beb1026fb"
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import functools"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def flatten_boxes(boxes):\n",
    "    return functools.reduce(\n",
    "        lambda m, box: m + list(map(lambda side: f'{box[0]} {side}',list(box[1])))\n",
    "    , boxes, [])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def remove_move(boxes, move):\n",
    "    move_box, move_side = move.split(' ')\n",
    "    clone = boxes[:]\n",
    "\n",
    "    for i, box in enumerate(clone):\n",
    "        if box[0] == move_box:\n",
    "            new_sides = box[1].replace(move_side, '')\n",
    "            clone[i] = (box[0], new_sides) if new_sides != '' else None\n",
    "            break\n",
    "\n",
    "    nonone = list(filter(lambda b: not (b is None), clone))\n",
    "\n",
    "    return nonone"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_candidate_closed_by(box, move):\n",
    "    move_box, move_side = move.split(' ')\n",
    "\n",
    "    opposites = {\n",
    "        'T': 'B',\n",
    "        'B': 'T',\n",
    "        'L': 'R',\n",
    "        'R': 'L'\n",
    "    }\n",
    "\n",
    "    if box[0] == move_box and box[1] == move_side: # closes box\n",
    "        return True\n",
    "    if box[0] != move_box and box[1] == opposites[move_side] and move_box[0] == box[0][0]: # closes same cloumn\n",
    "        return True\n",
    "    elif box[0] != move_box and box[1] == opposites[move_side] and move_box[1] == box[0][1]: # closes same row\n",
    "        return True\n",
    "\n",
    "    return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def closed_boxes(boxes, move):\n",
    "    candidates = list(filter(lambda b: len(b[1]) == 1, boxes))\n",
    "    closed = list(filter(lambda b: is_candidate_closed_by(b, move), candidates))\n",
    "\n",
    "    return len(closed)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# boxes [('A1', 'LTRB'), ('A2', 'LTRB'), ('B1', 'LTRB'), ('B2', 'LTRB')]\n",
    "def minimax(boxes, max_turn, max_score, min_score):\n",
    "    if len(boxes) == 0:\n",
    "        return max_score - min_score\n",
    "\n",
    "    if max_turn:\n",
    "        max_eval = -1000\n",
    "        children =  flatten_boxes(boxes)\n",
    "        for move in children:\n",
    "            new_moves = remove_move(boxes, move)\n",
    "            new_max_score = max_score + closed_boxes(boxes, move)\n",
    "            rating = minimax(new_moves, not max_turn, new_max_score, min_score)\n",
    "            max_eval = max(rating, max_eval)\n",
    "        return max_eval\n",
    "    else:\n",
    "        min_eval = 1000\n",
    "        children =  flatten_boxes(boxes)\n",
    "        for move in children:\n",
    "            new_moves = remove_move(boxes, move)\n",
    "            new_min_score = min_score + closed_boxes(boxes, move)\n",
    "            rating = minimax(new_moves, not max_turn, max_score, new_min_score)\n",
    "            min_eval = min(rating, min_eval)\n",
    "        return min_eval\n",
    "minimax([('A1', 'LTRB'), ('A2', 'LTRB'), ('B1', 'LTRB'), ('B2', 'LTRB')], True, 0, 0)\n",
    "\n"
   ]
  }
 ]
}