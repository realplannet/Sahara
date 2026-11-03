# Sahara catalogue — prices/services taken from the existing Sahara site. Descriptive copy is draft, flagged for review.
PHONE = "971501234567"
PHONE_DISPLAY = "+971 50 123 4567"
EMAIL = "info@saharabalinesespa.com"
FRESHA = "https://www.fresha.com/sahara-balinese"
INSTAGRAM = "https://www.instagram.com/saharabalinesespa"
BASE = "https://realplannet.github.io/Sahara"   # change when custom domain is attached
HOURS = "9:00 AM – 11:00 PM, 7 days"
MIN_ORDER = 250

# id, name, blurb, [(minutes, price)], cat, 'from' flag
ITEMS = [
 # Massage
 ("balinese","Balinese Massage","Deep rhythmic strokes with warm Balinese oil",[(60,300),(90,350)],"massage"),
 ("aromatherapy","Aromatherapy Massage","Essential oil blend tailored to your mood and needs",[(60,300),(90,350)],"massage"),
 ("deep-tissue","Deep Tissue Massage","Targets deep muscle layers, relieves chronic tension",[(60,300),(90,350)],"massage"),
 ("hot-stone","Hot Stone Massage","Heated basalt stones melt away deep muscle stress",[(60,350),(90,400)],"massage"),
 ("thai","Thai Massage","Stretch-based therapy to improve flexibility and energy",[(60,300),(90,350)],"massage"),
 ("prenatal","Prenatal Massage","Gentle and safe for expecting mothers (after 12 weeks)",[(60,300)],"massage"),
 ("cupping","Cupping Therapy","Promotes circulation and deep muscle recovery",[(45,220)],"massage"),
 ("shiatsu","Shiatsu Massage","Japanese pressure-point therapy for stress relief",[(60,300),(90,350)],"massage"),
 ("sports","Sports Massage","Performance recovery and injury prevention",[(60,300)],"massage"),
 ("reflexology","Foot Reflexology","Targeted pressure points to rebalance the whole body",[(45,200),(60,250)],"massage"),
 # Facials
 ("classic-facial","Classic Cleansing Facial","Deep cleanse, exfoliation, extractions, hydration mask",[(60,280)],"facial"),
 ("hydration-facial","Hydration Facial","Intensive moisture boost with hyaluronic serum",[(75,320)],"facial"),
 ("anti-ageing-facial","Anti-Ageing Facial","Lifting, firming and collagen-stimulating treatment",[(75,380)],"facial"),
 ("brightening-facial","Brightening Facial","Targets hyperpigmentation for an even, luminous skin tone",[(60,300)],"facial"),
 ("skin-rejuvenation","Skin Rejuvenation","Advanced multi-step resurfacing and renewal protocol",[(90,420)],"facial"),
 # Body
 ("body-scrub","Full Body Scrub","Lava salt or coffee scrub to exfoliate and renew",[(60,280)],"body"),
 ("body-wrap","Body Wrap","Nourishing herbal wrap to hydrate and smooth skin",[(60,300)],"body"),
 ("anti-cellulite","Anti-Cellulite Treatment","Targeted massage with firming cream for problem areas",[(60,300)],"body"),
 ("detox-ritual","Detox Revitalising Ritual","Scrub + wrap + massage for full-body renewal",[(90,350)],"body"),
 # Hair (from prices)
 ("blow-dry","Blow Dry","Professional blow dry and finish",[(40,120)],"hair","30–45 min"),
 ("hair-treatment","Deep Hair Treatment","Repair, strengthen and restore damaged hair",[(45,180)],"hair","45 min"),
 ("colouring","Colouring","Full colour, roots or toning with premium products",[(90,350)],"hair","90+ min"),
 ("bridal-hair","Bridal Hair Styling","Bridal trial included. Up to 3 hours on wedding day.",[(90,400)],"hair","90+ min"),
 ("updo","Up-Do & Event Hair","Elegant updos for events, galas and special occasions",[(60,280)],"hair","60 min"),
 # Nails
 ("manicure","Classic Manicure","Shape, cuticle care, buff and polish",[(45,90)],"nails"),
 ("pedicure","Classic Pedicure","Soak, exfoliation, cuticle care, foot massage, polish",[(60,110)],"nails"),
 ("gel-manicure","Gel Manicure","Long-lasting gel colour with LED lamp",[(60,150)],"nails"),
 ("gel-pedicure","Gel Pedicure","Full pedicure with gel polish finish",[(75,180)],"nails"),
 ("mani-pedi","Mani + Pedi Combo","Classic manicure and pedicure together",[(90,180)],"nails"),
 # Waxing (single price, no duration)
 ("wax-full-leg","Waxing — Full Leg","Strip or stripless wax",[(0,110)],"waxing"),
 ("wax-half-leg","Waxing — Half Leg","Strip or stripless wax",[(0,75)],"waxing"),
 ("wax-bikini","Waxing — Bikini","Strip or stripless wax",[(0,90)],"waxing"),
 ("wax-brazilian","Waxing — Brazilian","Strip or stripless wax",[(0,150)],"waxing"),
 ("wax-underarm","Waxing — Underarm","Strip or stripless wax",[(0,45)],"waxing"),
 ("wax-lip","Waxing — Upper Lip","Strip or stripless wax",[(0,35)],"waxing"),
 ("wax-face","Waxing — Full Face","Strip or stripless wax",[(0,90)],"waxing"),
 ("wax-body","Waxing — Full Body","Strip or stripless wax",[(0,280)],"waxing"),
]
CATS = {
 "massage":("Massage Therapy","From the ancient healing traditions of Bali to modern therapeutic techniques. All treatments use premium Balinese oils and are performed by certified therapists.","massage"),
 "facial":("Facial Treatments","Clinical-grade facials using premium skincare formulations, customised to your skin type after a brief consultation.","facials"),
 "body":("Body Rituals","Full-body treatments that exfoliate, detoxify and nourish, using Balinese botanicals — volcanic ash, coffee, turmeric and coconut.","body-rituals"),
 "hair":("Hair & Styling","Professional hair services from styling to colour, delivered to your home or hotel room — ideal before events and weddings.","hair-styling"),
 "nails":("Nail Care","Perfectly polished nails wherever you are. Our technicians arrive with professional equipment, premium polishes and sanitised tools.","nail-care"),
 "waxing":("Waxing","Premium strip and stripless wax, in the privacy of your own space.","waxing"),
}
def items(cat): return [i for i in ITEMS if i[4]==cat]
def item(id_): return next(i for i in ITEMS if i[0]==id_)
def frm(it):
    return min(p for _,p in it[3])
def dur_label(it):
    if len(it)>5: return it[5]
    o=it[3]
    if o[0][0]==0: return ""
    return " / ".join(str(m) for m,_ in o)+" min"
def price_label(it):
    o=it[3]
    s=" / ".join(f"AED {p}" for _,p in o)
    return ("From " if it[4]=="hair" else "")+s

PACKAGES = [
 ("I","The Sahara Ritual","Our most comprehensive single-guest experience",["60-min Balinese Massage with premium Balinese oil blend","45-min Signature Facial (personalised to your skin type)","45-min Full Body Scrub with lava salt or coffee","All premium products, towels and equipment included"],"150 minutes",600),
 ("II","Bali Serenity","The perfect 90-minute escape from daily life",["60-min Aromatherapy Massage with mood-blended essential oils","30-min Signature Facial Treatment","All premium products and equipment included"],"90 minutes",350),
 ("III","Couples Sanctuary","Side-by-side luxury for you and the one you love",["Dual 90-min Balinese or Hot Stone Massage (your choice)","Two therapists arrive simultaneously","Full set of premium products and equipment for both","Can be upgraded to include facials (+AED 250)"],"90 minutes · 2 guests",600),
 ("IV","The Royal Indulgence","The pinnacle of the Sahara experience",["60-min Deep Tissue Massage targeting key tension areas","45-min Full Body Lava Salt Scrub","45-min Anti-Ageing or Brightening Facial","All products, towels and professional setup included"],"150 minutes",750),
]
BRIDAL = [
 ("The Essential","Bridal Glow","Perfect for the bride in the days before the wedding",["Brightening Facial Treatment","Classic Manicure & Pedicure","Professional Blow Dry & Finish"],"2.5 hours · 1 guest",450),
 ("Day Before","Calm & Radiant","Relaxation and radiance the evening before your wedding",["60-min Aromatherapy Relaxation Massage","Full Body Lava Salt Scrub","Gel Manicure in your chosen shade"],"3 hours · 1 guest",550),
 ("For the Bridal Party","Bride & Tribe","Celebrate together with the whole bridal squad",["Full bridal facial for the bride","Mini relaxation massage for up to 3 bridesmaids","Mani-Pedi for bride, manicure for party"],"3 hours · up to 4 guests",800),
 ("The Ultimate","The Full Bridal Experience","Everything a bride could want, from head to toe",["Aromatherapy Massage & Full Body Scrub","Brightening Facial with LED mask","Gel Mani & Pedi · Bridal Hair Styling"],"4+ hours · 1 guest",900),
]
THERAPISTS = [
 ("Neny T.","Founder & Master Therapist","Balinese Massage · Hot Stone · Facials","Born in Ubud, Bali. 20+ years across luxury resorts and five-star hotels in Bali, Europe, Asia and the UAE. Personally trains and certifies every Sahara therapist."),
 ("Wayan S.","Senior Therapist","Deep Tissue · Thai · Cupping","Certified senior therapist trained to Neny's five-star protocol."),
 ("Putu A.","Beauty Specialist","Facials · Body Rituals · Waxing","Certified beauty specialist trained to Neny's five-star protocol."),
 ("Made K.","Nail & Hair Specialist","Manicure · Pedicure · Styling","Certified nail and hair specialist trained to Neny's five-star protocol."),
]
AREAS = ["Dubai Marina","JBR","Palm Jumeirah","Bluewaters","Downtown Dubai","Business Bay","DIFC","City Walk","Jumeirah","Umm Suqeim","Al Barsha","Dubai Hills","Arabian Ranches","Meydan","JVC","JLT","Mirdif","Al Quoz"]
FAQS = [
 ("What areas of Dubai do you cover?","We cover all of Dubai — Dubai Marina, JBR, Palm Jumeirah, Bluewaters, Downtown, Business Bay, DIFC, City Walk, Jumeirah, Umm Suqeim, Al Barsha, Dubai Hills, Arabian Ranches, Meydan, JVC, JLT, Mirdif, Al Quoz, and all gated communities and hotels. If you're unsure, WhatsApp us your location and we'll confirm within minutes."),
 ("How far in advance do I need to book?","We accept same-day bookings — simply book via Fresha or WhatsApp us directly. For peak times (weekends, evenings and holidays) we recommend booking 24–48 hours ahead to secure your preferred time slot. Bridal and group bookings require at least 1 week's notice."),
 ("What do I need to prepare at home?","Very little. We bring everything — our own professional massage table, fresh towels and linens, all Balinese oils and products, and any specialist equipment for the booked treatments. All we ask is a clear space of approximately 2m × 2m for the massage table, and access to your space a few minutes before the session starts."),
 ("Are your therapists female? Can men book?","All of our current therapists are female. We welcome male clients for all massage and wellness services — please note when booking so we can ensure the session is conducted appropriately. For couples bookings both guests are fully welcomed."),
 ("Are your therapists certified?","Yes. Every Sahara therapist holds professional certifications in their respective disciplines and has been personally trained and approved by our founder Neny Trisnayanti — who brings 20+ years of five-star hotel wellness experience. All therapists are background-verified and fully insured."),
 ("Can I book for a hotel room or villa?","Absolutely — this is one of our most popular setups. We regularly serve guests at hotels across Dubai. Simply provide your hotel name, room number and check-in status when booking. Poolside and cabana sessions are available at many properties — enquire via WhatsApp for arrangements."),
 ("How do I pay?","Payment is accepted via Fresha (card on booking), cash on the day, or bank transfer for group/bridal packages. All prices are inclusive of therapist travel within Dubai. A minimum booking value of AED 250 applies per session."),
 ("What is your cancellation policy?","We ask for a minimum of 3 hours' notice for cancellations or reschedules. Cancellations with less than 3 hours' notice may incur a 50% charge. Bridal and group bookings require 48 hours' notice for a full refund. We understand emergencies happen — please contact us as soon as possible and we will always do our best to accommodate you."),
 ("Can I request the same therapist each time?","Yes — we always try to honour therapist preferences. When booking via WhatsApp, simply mention your preferred therapist by name. Availability cannot be guaranteed but we will always try our best. Many of our regular clients build a wonderful long-term relationship with their preferred Sahara therapist."),
 ("Do you offer gift vouchers?","Yes. Sahara gift vouchers are available for any amount or specific treatment. They make the perfect gift for birthdays, Mother's Day, Eid, and other special occasions. Request one on our gift voucher page or via WhatsApp — we can provide a beautifully designed digital certificate within 24 hours."),
]
# Per-treatment page copy (draft — review before publishing)
TX = {
 "balinese":dict(what="Balinese massage is the signature healing massage of Bali. Long, flowing strokes are combined with gentle stretching, acupressure and kneading, all with warm Balinese oil. Pressure is medium — firm enough to release tension, soft enough to switch off completely.",best=["First-time clients","Stress and general tension","Couples and special occasions","A full-body reset"],pressure="Medium",faq=[("What is the difference between Balinese and Thai massage?","Balinese massage is done on a table with oil and long flowing strokes plus acupressure. Thai massage is traditionally clothed and stretch-based, so it is more active."),("How firm is it?","Medium, and your therapist adjusts it to you. For firmer work on knots choose Deep Tissue.")]),
 "aromatherapy":dict(what="A slow, soothing full-body massage led by essential oils blended to your mood — calming, uplifting or restorative. Strokes are softer and more rhythmic, designed for deep relaxation.",best=["Stress and busy minds","Light-pressure lovers","Evening wind-down","Gifts"],pressure="Soft to medium",faq=[("Can I choose my oils?","Yes — tell your therapist how you want to feel and she will blend accordingly. Let us know about any allergies when booking.")]),
 "deep-tissue":dict(what="Slow, firm pressure targeting the deeper layers of muscle and connective tissue to ease chronic tension, knots and stiffness in the back, neck and shoulders.",best=["Desk-related tension","Knots and stiffness","Active people","Chronic tightness"],pressure="Firm",faq=[("Will it hurt?","Deep tissue is firm but should never be painful. Tell your therapist at any time if you want it lighter.")]),
 "hot-stone":dict(what="Smooth heated basalt stones are placed on and glided over the body to warm tight muscles, allowing the therapist to work more deeply and the body to let go.",best=["Cold-sensitive muscles","Deep relaxation","Tension in back and shoulders","Cooler evenings"],pressure="Medium",faq=[("Is it suitable for everyone?","Heat is not suitable for everyone — please mention any medical condition, circulation issue or skin sensitivity when booking.")]),
 "thai":dict(what="A stretch-based therapy combining compression, rhythmic pressure and assisted stretching to improve flexibility, release tension and restore energy flow.",best=["Stiff, tight bodies","Flexibility","Active people","Those who prefer less oil"],pressure="Medium to firm",faq=[("Do I undress?","Please let us know your preference when booking; the therapist will arrange the session accordingly.")]),
 "prenatal":dict(what="A gentle, supportive massage for mums-to-be, designed to ease the common aches of pregnancy. Sahara offers prenatal massage after 12 weeks of pregnancy.",best=["Back, hip and leg aches","Swelling and heavy legs","Relaxation before birth"],pressure="Soft to medium",faq=[("When can I have a prenatal massage?","Sahara offers prenatal massage after 12 weeks. Please consult your doctor first if you have any complications or concerns.")]),
 "cupping":dict(what="Cupping uses gentle suction to lift tissue and encourage circulation, helping to release stubborn tightness in the back and shoulders.",best=["Back and shoulder tightness","Muscle recovery","Circulation support"],pressure="Targeted",faq=[("Does it leave marks?","Cupping can leave temporary round marks on the skin. They typically fade within days.")]),
 "shiatsu":dict(what="A Japanese pressure-point therapy using rhythmic finger and palm pressure along the body's energy pathways to relieve stress and restore balance.",best=["Stress relief","Mental calm","Those who prefer firm, precise pressure"],pressure="Medium to firm",faq=[("Is oil used?","Shiatsu is traditionally performed without heavy oils. Confirm preferences when booking.")]),
 "sports":dict(what="Firm techniques and stretching to support recovery, ease sore muscles and help prevent injury for runners, gym-goers and weekend athletes.",best=["Post-training recovery","Muscle soreness","Injury prevention"],pressure="Firm",faq=[("When should I book?","Many clients book 24–48 hours after intense training. Tell us about any injury when booking.")]),
 "reflexology":dict(what="Targeted pressure on points of the feet linked to the rest of the body, to rebalance and relax. A calming treatment after a long day on your feet.",best=["Tired, heavy legs","Quick reset","Those who want a lighter treatment"],pressure="Medium",faq=[("Which duration should I choose?","45 minutes is a focused reset; 60 minutes allows a more complete treatment.")]),
}
