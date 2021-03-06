#MenuTitle: Align Selection to Baseline
"""Align selected paths (and parts of paths) in the frontmost layer to the Baseline."""

import GlyphsApp

Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedLayer = Font.selectedLayers[0]

try:
	selection = selectedLayer.selection()
	lowestY = min( ( n.y for n in selection ) )

	Font.disableUpdateInterface()

	for thisNode in selection:
		thisNode.y -= lowestY

	Font.enableUpdateInterface()
	
except Exception, e:
	print "Error: Nothing selected in frontmost layer?"
	print e
