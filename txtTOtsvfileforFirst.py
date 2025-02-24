# Define the input data
consensus_sequence = "MRGGEAARCHMLQTSNYSLVLSLQFLLLFYDLFVNSFSELLRLAPVIQLVLFIIQDIAILFNVIIIFLMFFNTGAFQAGLRPGLFTRGRGGRGGARTAAPPSTSGSASRPRGRWLPRMQFPWGLKMAALFVFPRASATGKGRPARAKEGPPAAGFRGNANAAALLGEEPEVCKRKIAILGVLSSTPLEILFFLNGWYYATYFLLELFIFLYKACLFTARQKSLQALTFVLAGLLLPYPTANLVLDVVMLLLYLGIEVIRLFFGQADQAEMRRLQKLCDTGTKGNLCQRKMPLGISVALTFPSAMMASYYLLLQTYVLRLEAIMNGILLFFCGSELLLEVGQDLTLAAFSRQCRAEGAKAIRRGRCRIRGICRTSRACVLSAGFLWTRRRSSSPSSPTVAAIMLLKGSDRQKSKTPAVANQLPVPSGGMCMKKDEQRRLLLYCYFWTDCQANRRRGSPILVRSQVGPVVYFKICLGQPNESRTAAERSSRSQTCAEKMRLGSKRCAPAHQKLLIGL"

amino_acid_scores = {
1: {'M': 0.004},
2: {'R': 0.002},
3: {'G': 0.002},
4: {'G': 0.002},
5: {'E': 0.002},
6: {'A': 0.002},
7: {'A': 0.002},
8: {'R': 0.002},
9: {'C': 0.002},
10: {'H': 0.002},
11: {'M': 0.01},
12: {'L': 0.01},
13: {'Q': 0.01},
14: {'T': 0.01},
15: {'S': 0.01},
16: {'N': 0.01},
17: {'Y': 0.01},
18: {'S': 0.01},
19: {'L': 0.014},
20: {'V': 0.01},
21: {'L': 0.01},
22: {'S': 0.01},
23: {'L': 0.014},
24: {'Q': 0.01},
25: {'F': 0.012},
26: {'L': 0.01},
27: {'L': 0.01},
28: {'L': 0.01},
29: {'F': 0.008},
30: {'Y': 0.008},
31: {'D': 0.012},
32: {'L': 0.016},
33: {'F': 0.01},
34: {'V': 0.01},
35: {'N': 0.01},
36: {'S': 0.01},
37: {'F': 0.01},
38: {'S': 0.01},
39: {'E': 0.01},
40: {'L': 0.01},
41: {'L': 0.012},
42: {'R': 0.012},
43: {'L': 0.006},
44: {'A': 0.01},
45: {'P': 0.01},
46: {'V': 0.01},
47: {'I': 0.006},
48: {'Q': 0.012},
49: {'L': 0.014},
50: {'V': 0.012},
51: {'L': 0.01},
52: {'F': 0.01},
53: {'I': 0.01},
54: {'I': 0.01},
55: {'Q': 0.01},
56: {'D': 0.01},
57: {'I': 0.01},
58: {'A': 0.012},
59: {'I': 0.008},
60: {'L': 0.012},
61: {'F': 0.01},
62: {'N': 0.01},
63: {'V': 0.01},
64: {'I': 0.01},
65: {'I': 0.01},
66: {'I': 0.006},
67: {'F': 0.012},
68: {'L': 0.018},
69: {'M': 0.01},
70: {'F': 0.01},
71: {'F': 0.012},
72: {'N': 0.01},
73: {'T': 0.016},
74: {'G': 0.01},
75: {'A': 0.01},
76: {'F': 0.01},
77: {'Q': 0.01},
78: {'A': 0.012},
79: {'G': 0.01},
80: {'L': 0.012},
81: {'R': 0.014},
82: {'P': 0.01},
83: {'G': 0.012},
84: {'L': 0.016},
85: {'F': 0.01},
86: {'T': 0.012},
87: {'R': 0.01},
88: {'G': 0.014},
89: {'R': 0.014},
90: {'G': 0.022},
91: {'G': 0.014},
92: {'R': 0.012},
93: {'G': 0.024},
94: {'G': 0.014},
95: {'A': 0.02},
96: {'R': 0.012},
97: {'T': 0.02},
98: {'A': 0.028},
99: {'A': 0.02},
100: {'P': 0.022},
101: {'P': 0.02},
102: {'S': 0.03},
103: {'T': 0.02},
104: {'S': 0.042},
105: {'G': 0.028},
106: {'S': 0.02},
107: {'A': 0.024},
108: {'S': 0.03},
109: {'R': 0.038},
110: {'P': 0.02},
111: {'R': 0.028},
112: {'G': 0.022},
113: {'R': 0.044},
114: {'W': 0.022},
115: {'L': 0.024},
116: {'P': 0.032},
117: {'R': 0.038},
118: {'M': 0.064},
119: {'Q': 0.094},
120: {'F': 0.114},
121: {'P': 0.138},
122: {'W': 0.116},
123: {'G': 0.118},
124: {'L': 0.118},
125: {'K': 0.096},
126: {'M': 0.652},
127: {'A': 0.654},
128: {'A': 0.018},
129: {'L': 0.022},
130: {'F': 0.018},
131: {'V': 0.012},
132: {'F': 0.016},
133: {'P': 0.55},
134: {'R': 0.616},
135: {'A': 0.002},
136: {'S': 0.002},
137: {'A': 0.002},
138: {'T': 0.002},
139: {'G': 0.002},
140: {'K': 0.002},
141: {'G': 0.002},
142: {'R': 0.002},
143: {'P': 0.002},
144: {'A': 0.002},
145: {'R': 0.002},
146: {'A': 0.002},
147: {'K': 0.002},
148: {'E': 0.002},
149: {'G': 0.002},
150: {'P': 0.006},
151: {'P': 0.004},
152: {'A': 0.002},
153: {'A': 0.002},
154: {'G': 0.002},
155: {'F': 0.004},
156: {'R': 0.002},
157: {'G': 0.004},
158: {'N': 0.002},
159: {'A': 0.002},
160: {'N': 0.002},
161: {'A': 0.002},
162: {'A': 0.006},
163: {'A': 0.004},
164: {'L': 0.004},
165: {'L': 0.014},
166: {'G': 0.534},
167: {'E': 0.006},
168: {'E': 0.004},
169: {'P': 0.006},
170: {'E': 0.006},
171: {'V': 0.01},
172: {'C': 0.01},
173: {'K': 0.424},
174: {'R': 0.516},
175: {'K': 0.006},
176: {'I': 0.012},
177: {'A': 0.004},
178: {'I': 0.006},
179: {'L': 0.624},
180: {'G': 0.02},
181: {'V': 0.026},
182: {'L': 0.034},
183: {'S': 0.756},
184: {'S': 0.748},
185: {'T': 0.596},
186: {'P': 0.718},
187: {'L': 0.776},
188: {'E': 0.642},
189: {'I': 0.552},
190: {'L': 0.78},
191: {'F': 0.476},
192: {'F': 0.744},
193: {'L': 0.782},
194: {'N': 0.776},
195: {'G': 0.712},
196: {'W': 0.784},
197: {'Y': 0.782},
198: {'Y': 0.502},
199: {'A': 0.774},
200: {'T': 0.706},
201: {'Y': 0.73},
202: {'F': 0.776},
203: {'L': 0.712},
204: {'L': 0.698},
205: {'E': 0.786},
206: {'L': 0.494},
207: {'F': 0.628},
208: {'I': 0.524},
209: {'F': 0.796},
210: {'L': 0.492},
211: {'Y': 0.794},
212: {'K': 0.798},
213: {'A': 0.002},
214: {'C': 0.002},
215: {'L': 0.002},
216: {'F': 0.002},
217: {'T': 0.002},
218: {'A': 0.002},
219: {'R': 0.002},
220: {'Q': 0.002},
221: {'K': 0.002},
222: {'S': 0.002},
223: {'L': 0.002},
224: {'Q': 0.002},
225: {'A': 0.006},
226: {'L': 0.006},
227: {'T': 0.006},
228: {'F': 0.004},
229: {'V': 0.006},
230: {'L': 0.006},
231: {'A': 0.028},
232: {'G': 0.606},
233: {'L': 0.7},
234: {'L': 0.772},
235: {'L': 0.812},
236: {'P': 0.812},
237: {'Y': 0.808},
238: {'P': 0.778},
239: {'T': 0.498},
240: {'A': 0.684},
241: {'N': 0.822},
242: {'L': 0.822},
243: {'V': 0.55},
244: {'L': 0.814},
245: {'D': 0.808},
246: {'V': 0.59},
247: {'V': 0.692},
248: {'M': 0.844},
249: {'L': 0.992},
250: {'L': 0.532},
251: {'L': 0.982},
252: {'Y': 0.968},
253: {'L': 0.978},
254: {'G': 0.996},
255: {'I': 0.82},
256: {'E': 0.996},
257: {'V': 0.768},
258: {'I': 0.706},
259: {'R': 0.992},
260: {'L': 0.7},
261: {'F': 0.978},
262: {'F': 0.934},
263: {'G': 0.008},
264: {'Q': 0.004},
265: {'A': 0.004},
266: {'D': 0.004},
267: {'Q': 0.004},
268: {'A': 0.004},
269: {'E': 0.004},
270: {'M': 0.004},
271: {'R': 0.004},
272: {'R': 0.004},
273: {'L': 0.004},
274: {'Q': 0.004},
275: {'K': 0.004},
276: {'L': 0.008},
277: {'C': 0.004},
278: {'D': 0.004},
279: {'T': 0.008},
280: {'G': 0.98},
281: {'T': 0.674},
282: {'K': 0.982},
283: {'G': 1.0},
284: {'N': 0.996},
285: {'L': 0.992},
286: {'C': 0.966},
287: {'Q': 0.956},
288: {'R': 0.962},
289: {'K': 0.898},
290: {'M': 0.708},
291: {'P': 0.95},
292: {'L': 0.996},
293: {'G': 0.54},
294: {'I': 0.864},
295: {'S': 0.976},
296: {'V': 0.568},
297: {'A': 0.918},
298: {'L': 0.956},
299: {'T': 0.926},
300: {'F': 0.774},
301: {'P': 0.994},
302: {'S': 0.72},
303: {'A': 0.896},
304: {'M': 0.64},
305: {'M': 0.898},
306: {'A': 0.978},
307: {'S': 0.646},
308: {'Y': 1.0},
309: {'Y': 0.976},
310: {'L': 0.94},
311: {'L': 0.99},
312: {'L': 0.976},
313: {'Q': 1.0},
314: {'T': 1.0},
315: {'Y': 0.972},
316: {'V': 0.772},
317: {'L': 0.994},
318: {'R': 0.986},
319: {'L': 0.988},
320: {'E': 0.998},
321: {'A': 0.924},
322: {'I': 0.814},
323: {'M': 0.682},
324: {'N': 0.862},
325: {'G': 0.358},
326: {'I': 0.964},
327: {'L': 0.97},
328: {'L': 0.994},
329: {'F': 0.578},
330: {'F': 0.992},
331: {'C': 0.686},
332: {'G': 0.726},
333: {'S': 0.642},
334: {'E': 0.996},
335: {'L': 0.916},
336: {'L': 0.87},
337: {'L': 0.994},
338: {'E': 0.666},
339: {'V': 0.658},
340: {'G': 0.01},
341: {'Q': 0.014},
342: {'D': 0.01},
343: {'L': 0.882},
344: {'T': 0.78},
345: {'L': 0.946},
346: {'A': 0.592},
347: {'A': 0.554},
348: {'F': 0.966},
349: {'S': 0.938},
350: {'R': 0.002},
351: {'Q': 0.004},
352: {'C': 0.002},
353: {'R': 0.002},
354: {'A': 0.002},
355: {'E': 0.002},
356: {'G': 0.002},
357: {'A': 0.002},
358: {'K': 0.002},
359: {'A': 0.002},
360: {'I': 0.002},
361: {'R': 0.002},
362: {'R': 0.002},
363: {'G': 0.004},
364: {'R': 0.006},
365: {'C': 0.006},
366: {'R': 0.004},
367: {'I': 0.006},
368: {'R': 0.008},
369: {'G': 0.008},
370: {'I': 0.008},
371: {'C': 0.008},
372: {'R': 0.022},
373: {'T': 0.01},
374: {'S': 0.012},
375: {'R': 0.012},
376: {'A': 0.012},
377: {'C': 0.014},
378: {'V': 0.012},
379: {'L': 0.012},
380: {'S': 0.014},
381: {'A': 0.022},
382: {'G': 0.012},
383: {'F': 0.02},
384: {'L': 0.018},
385: {'W': 0.014},
386: {'T': 0.012},
387: {'R': 0.026},
388: {'R': 0.022},
389: {'R': 0.022},
390: {'S': 0.016},
391: {'S': 0.752},
392: {'S': 0.024},
393: {'P': 0.02},
394: {'S': 0.016},
395: {'S': 0.014},
396: {'P': 0.018},
397: {'T': 0.016},
398: {'V': 0.014},
399: {'A': 0.014},
400: {'A': 0.02},
401: {'I': 0.032},
402: {'M': 0.458},
403: {'L': 0.004},
404: {'L': 0.012},
405: {'K': 0.01},
406: {'G': 0.01},
407: {'S': 0.022},
408: {'D': 0.666},
409: {'R': 0.548},
410: {'Q': 0.002},
411: {'K': 0.002},
412: {'S': 0.002},
413: {'K': 0.002},
414: {'T': 0.002},
415: {'P': 0.002},
416: {'A': 0.002},
417: {'V': 0.002},
418: {'A': 0.002},
419: {'N': 0.002},
420: {'Q': 0.002},
421: {'L': 0.002},
422: {'P': 0.002},
423: {'V': 0.002},
424: {'P': 0.002},
425: {'S': 0.002},
426: {'G': 0.002},
427: {'G': 0.002},
428: {'M': 0.002},
429: {'C': 0.002},
430: {'M': 0.002},
431: {'K': 0.002},
432: {'K': 0.002},
433: {'D': 0.002},
434: {'E': 0.002},
435: {'Q': 0.002},
436: {'R': 0.002},
437: {'R': 0.002},
438: {'L': 0.002},
439: {'L': 0.002},
440: {'L': 0.002},
441: {'Y': 0.002},
442: {'C': 0.002},
443: {'Y': 0.002},
444: {'F': 0.002},
445: {'W': 0.002},
446: {'T': 0.002},
447: {'D': 0.002},
448: {'C': 0.002},
449: {'Q': 0.002},
450: {'A': 0.002},
451: {'N': 0.002},
452: {'R': 0.002},
453: {'R': 0.002},
454: {'R': 0.002},
455: {'G': 0.004},
456: {'S': 0.004},
457: {'P': 0.01},
458: {'I': 0.492},
459: {'L': 0.024},
460: {'V': 0.024},
461: {'R': 0.016},
462: {'S': 0.03},
463: {'Q': 0.012},
464: {'V': 0.016},
465: {'G': 0.016},
466: {'P': 0.016},
467: {'V': 0.012},
468: {'V': 0.022},
469: {'Y': 0.012},
470: {'F': 0.016},
471: {'K': 0.012},
472: {'I': 0.012},
473: {'C': 0.01},
474: {'L': 0.016},
475: {'G': 0.008},
476: {'Q': 0.008},
477: {'P': 0.008},
478: {'N': 0.012},
479: {'E': 0.004},
480: {'S': 0.012},
481: {'R': 0.008},
482: {'T': 0.008},
483: {'A': 0.004},
484: {'A': 0.008},
485: {'E': 0.004},
486: {'R': 0.004},
487: {'S': 0.006},
488: {'S': 0.006},
489: {'R': 0.004},
490: {'S': 0.004},
491: {'Q': 0.004},
492: {'T': 0.008},
493: {'C': 0.004},
494: {'A': 0.006},
495: {'E': 0.004},
496: {'K': 0.004},
497: {'M': 0.004},
498: {'R': 0.004},
499: {'L': 0.004},
500: {'G': 0.004},
501: {'S': 0.006},
502: {'K': 0.004},
503: {'R': 0.006},
504: {'C': 0.004},
505: {'A': 0.004},
506: {'P': 0.004},
507: {'A': 0.002},
508: {'H': 0.002},
509: {'Q': 0.002},
510: {'K': 0.002},
511: {'L': 0.002},
512: {'L': 0.002},
513: {'I': 0.002},
514: {'G': 0.002},
515: {'L': 0.002}
}

# Convert the data to the desired format
tsv_data = "Position\tConsensus Aminoacid\tConservation Score\n"

for position, scores in amino_acid_scores.items():
    amino_acid = max(scores, key=scores.get)
    conservation_score = scores[amino_acid]
    tsv_data += f"{position}\t{amino_acid}\t{conservation_score}\n"

# Write the data to a TSV file
with open("output.tsv", "w") as tsv_file:
    tsv_file.write(tsv_data)

