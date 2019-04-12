from django.db import models

# Create your models here.
class Drugs(models.Model):
    drugid = models.BigIntegerField(db_index = True, db_column='DrugID')  # Field name made lowercase.
    drugname = models.CharField(db_index = True, db_column='DrugName', primary_key=True, max_length=50)  # Field name made lowercase.
    isopioid = models.BooleanField(db_index = True, db_column='IsOpioid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Drugs'


class Prescriber(models.Model):
    prescriberid = models.AutoField(db_index = True, db_column='PrescriberID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_index = True, db_column='Fname', verbose_name='First Name', max_length=11, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_index = True, db_column='Lname', verbose_name='Last Name', max_length=11, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_index = True, db_column='Gender', max_length=2, blank=True, null=True)  # Field name made lowercase.
    state = models.ForeignKey('Statedata', models.DO_NOTHING, db_index = True, db_column='State')  # Field name made lowercase.
    credentials = models.CharField(db_index = True, db_column='Credentials', max_length=20, blank=True, null=True)  # Field name made lowercase.
    specialty = models.CharField(db_index = True, db_column='Specialty', max_length=62, blank=True, null=True)  # Field name made lowercase.
    opioid_prescriber = models.BooleanField(db_column='Opioid Prescriber', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    totalprescriptions = models.BigIntegerField(db_column='TotalPrescriptions', verbose_name='Total Prescriptions',blank=True, null=True)  # Field name made lowercase.
    abilify = models.IntegerField(db_column='ABILIFY', blank=True, null=True)  # Field name made lowercase.
    acetaminophen_codeine = models.IntegerField(db_column='ACETAMINOPHEN CODEINE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    acyclovir = models.IntegerField(db_column='ACYCLOVIR', blank=True, null=True)  # Field name made lowercase.
    advair_diskus = models.IntegerField(db_column='ADVAIR DISKUS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aggrenox = models.IntegerField(db_column='AGGRENOX', blank=True, null=True)  # Field name made lowercase.
    alendronate_sodium = models.IntegerField(db_column='ALENDRONATE SODIUM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    allopurinol = models.IntegerField(db_column='ALLOPURINOL', blank=True, null=True)  # Field name made lowercase.
    alprazolam = models.IntegerField(db_column='ALPRAZOLAM', blank=True, null=True)  # Field name made lowercase.
    amiodarone_hcl = models.IntegerField(db_column='AMIODARONE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amitriptyline_hcl = models.IntegerField(db_column='AMITRIPTYLINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amlodipine_besylate = models.IntegerField(db_column='AMLODIPINE BESYLATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amlodipine_besylate_benazepril = models.IntegerField(db_column='AMLODIPINE BESYLATE BENAZEPRIL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amoxicillin = models.IntegerField(db_column='AMOXICILLIN', blank=True, null=True)  # Field name made lowercase.
    amox_tr_potassium_clavulanate = models.IntegerField(db_column='AMOX TR POTASSIUM CLAVULANATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amphetamine_salt_combo = models.IntegerField(db_column='AMPHETAMINE SALT COMBO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    atenolol = models.IntegerField(db_column='ATENOLOL', blank=True, null=True)  # Field name made lowercase.
    atorvastatin_calcium = models.IntegerField(db_column='ATORVASTATIN CALCIUM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    avodart = models.IntegerField(db_column='AVODART', blank=True, null=True)  # Field name made lowercase.
    azithromycin = models.IntegerField(db_column='AZITHROMYCIN', blank=True, null=True)  # Field name made lowercase.
    baclofen = models.IntegerField(db_column='BACLOFEN', blank=True, null=True)  # Field name made lowercase.
    bd_ultra_fine_pen_needle = models.IntegerField(db_column='BD ULTRA FINE PEN NEEDLE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    benazepril_hcl = models.IntegerField(db_column='BENAZEPRIL HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    benicar = models.IntegerField(db_column='BENICAR', blank=True, null=True)  # Field name made lowercase.
    benicar_hct = models.IntegerField(db_column='BENICAR HCT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    benztropine_mesylate = models.IntegerField(db_column='BENZTROPINE MESYLATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bisoprolol_hydrochlorothiazide = models.IntegerField(db_column='BISOPROLOL HYDROCHLOROTHIAZIDE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    brimonidine_tartrate = models.IntegerField(db_column='BRIMONIDINE TARTRATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bumetanide = models.IntegerField(db_column='BUMETANIDE', blank=True, null=True)  # Field name made lowercase.
    bupropion_hcl_sr = models.IntegerField(db_column='BUPROPION HCL SR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bupropion_xl = models.IntegerField(db_column='BUPROPION XL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    buspirone_hcl = models.IntegerField(db_column='BUSPIRONE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bystolic = models.IntegerField(db_column='BYSTOLIC', blank=True, null=True)  # Field name made lowercase.
    carbamazepine = models.IntegerField(db_column='CARBAMAZEPINE', blank=True, null=True)  # Field name made lowercase.
    carbidopa_levodopa = models.IntegerField(db_column='CARBIDOPA LEVODOPA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    carisoprodol = models.IntegerField(db_column='CARISOPRODOL', blank=True, null=True)  # Field name made lowercase.
    cartia_xt = models.IntegerField(db_column='CARTIA XT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    carvedilol = models.IntegerField(db_column='CARVEDILOL', blank=True, null=True)  # Field name made lowercase.
    cefuroxime = models.IntegerField(db_column='CEFUROXIME', blank=True, null=True)  # Field name made lowercase.
    celebrex = models.IntegerField(db_column='CELEBREX', blank=True, null=True)  # Field name made lowercase.
    cephalexin = models.IntegerField(db_column='CEPHALEXIN', blank=True, null=True)  # Field name made lowercase.
    chlorhexidine_gluconate = models.IntegerField(db_column='CHLORHEXIDINE GLUCONATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chlorthalidone = models.IntegerField(db_column='CHLORTHALIDONE', blank=True, null=True)  # Field name made lowercase.
    cilostazol = models.IntegerField(db_column='CILOSTAZOL', blank=True, null=True)  # Field name made lowercase.
    ciprofloxacin_hcl = models.IntegerField(db_column='CIPROFLOXACIN HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    citalopram_hbr = models.IntegerField(db_column='CITALOPRAM HBR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    clindamycin_hcl = models.IntegerField(db_column='CLINDAMYCIN HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    clobetasol_propionate = models.IntegerField(db_column='CLOBETASOL PROPIONATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    clonazepam = models.IntegerField(db_column='CLONAZEPAM', blank=True, null=True)  # Field name made lowercase.
    clonidine_hcl = models.IntegerField(db_column='CLONIDINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    clopidogrel = models.IntegerField(db_column='CLOPIDOGREL', blank=True, null=True)  # Field name made lowercase.
    clotrimazole_betamethasone = models.IntegerField(db_column='CLOTRIMAZOLE BETAMETHASONE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    colcrys = models.IntegerField(db_column='COLCRYS', blank=True, null=True)  # Field name made lowercase.
    combivent_respimat = models.IntegerField(db_column='COMBIVENT RESPIMAT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    crestor = models.IntegerField(db_column='CRESTOR', blank=True, null=True)  # Field name made lowercase.
    cyclobenzaprine_hcl = models.IntegerField(db_column='CYCLOBENZAPRINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dexilant = models.IntegerField(db_column='DEXILANT', blank=True, null=True)  # Field name made lowercase.
    diazepam = models.IntegerField(db_column='DIAZEPAM', blank=True, null=True)  # Field name made lowercase.
    diclofenac_sodium = models.IntegerField(db_column='DICLOFENAC SODIUM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dicyclomine_hcl = models.IntegerField(db_column='DICYCLOMINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    digox = models.IntegerField(db_column='DIGOX', blank=True, null=True)  # Field name made lowercase.
    digoxin = models.IntegerField(db_column='DIGOXIN', blank=True, null=True)  # Field name made lowercase.
    diltiazem_24hr_cd = models.IntegerField(db_column='DILTIAZEM 24HR CD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diltiazem_24hr_er = models.IntegerField(db_column='DILTIAZEM 24HR ER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diltiazem_er = models.IntegerField(db_column='DILTIAZEM ER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diltiazem_hcl = models.IntegerField(db_column='DILTIAZEM HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diovan = models.IntegerField(db_column='DIOVAN', blank=True, null=True)  # Field name made lowercase.
    diphenoxylate_atropine = models.IntegerField(db_column='DIPHENOXYLATE ATROPINE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    divalproex_sodium = models.IntegerField(db_column='DIVALPROEX SODIUM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    divalproex_sodium_er = models.IntegerField(db_column='DIVALPROEX SODIUM ER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    donepezil_hcl = models.IntegerField(db_column='DONEPEZIL HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dorzolamide_timolol = models.IntegerField(db_column='DORZOLAMIDE TIMOLOL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    doxazosin_mesylate = models.IntegerField(db_column='DOXAZOSIN MESYLATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    doxepin_hcl = models.IntegerField(db_column='DOXEPIN HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    doxycycline_hyclate = models.IntegerField(db_column='DOXYCYCLINE HYCLATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    duloxetine_hcl = models.IntegerField(db_column='DULOXETINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    enalapril_maleate = models.IntegerField(db_column='ENALAPRIL MALEATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    escitalopram_oxalate = models.IntegerField(db_column='ESCITALOPRAM OXALATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    estradiol = models.IntegerField(db_column='ESTRADIOL', blank=True, null=True)  # Field name made lowercase.
    exelon = models.IntegerField(db_column='EXELON', blank=True, null=True)  # Field name made lowercase.
    famotidine = models.IntegerField(db_column='FAMOTIDINE', blank=True, null=True)  # Field name made lowercase.
    felodipine_er = models.IntegerField(db_column='FELODIPINE ER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fenofibrate = models.IntegerField(db_column='FENOFIBRATE', blank=True, null=True)  # Field name made lowercase.
    fentanyl = models.IntegerField(db_column='FENTANYL', blank=True, null=True)  # Field name made lowercase.
    finasteride = models.IntegerField(db_column='FINASTERIDE', blank=True, null=True)  # Field name made lowercase.
    flovent_hfa = models.IntegerField(db_column='FLOVENT HFA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fluconazole = models.IntegerField(db_column='FLUCONAZOLE', blank=True, null=True)  # Field name made lowercase.
    fluoxetine_hcl = models.IntegerField(db_column='FLUOXETINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fluticasone_propionate = models.IntegerField(db_column='FLUTICASONE PROPIONATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    furosemide = models.IntegerField(db_column='FUROSEMIDE', blank=True, null=True)  # Field name made lowercase.
    gabapentin = models.IntegerField(db_column='GABAPENTIN', blank=True, null=True)  # Field name made lowercase.
    gemfibrozil = models.IntegerField(db_column='GEMFIBROZIL', blank=True, null=True)  # Field name made lowercase.
    glimepiride = models.IntegerField(db_column='GLIMEPIRIDE', blank=True, null=True)  # Field name made lowercase.
    glipizide = models.IntegerField(db_column='GLIPIZIDE', blank=True, null=True)  # Field name made lowercase.
    glipizide_er = models.IntegerField(db_column='GLIPIZIDE ER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    glipizide_xl = models.IntegerField(db_column='GLIPIZIDE XL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    glyburide = models.IntegerField(db_column='GLYBURIDE', blank=True, null=True)  # Field name made lowercase.
    haloperidol = models.IntegerField(db_column='HALOPERIDOL', blank=True, null=True)  # Field name made lowercase.
    humalog = models.IntegerField(db_column='HUMALOG', blank=True, null=True)  # Field name made lowercase.
    hydralazine_hcl = models.IntegerField(db_column='HYDRALAZINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hydrochlorothiazide = models.IntegerField(db_column='HYDROCHLOROTHIAZIDE', blank=True, null=True)  # Field name made lowercase.
    hydrocodone_acetaminophen = models.IntegerField(db_column='HYDROCODONE ACETAMINOPHEN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hydrocortisone = models.IntegerField(db_column='HYDROCORTISONE', blank=True, null=True)  # Field name made lowercase.
    hydromorphone_hcl = models.IntegerField(db_column='HYDROMORPHONE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hydroxyzine_hcl = models.IntegerField(db_column='HYDROXYZINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ibandronate_sodium = models.IntegerField(db_column='IBANDRONATE SODIUM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ibuprofen = models.IntegerField(db_column='IBUPROFEN', blank=True, null=True)  # Field name made lowercase.
    insulin_syringe = models.IntegerField(db_column='INSULIN SYRINGE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ipratropium_bromide = models.IntegerField(db_column='IPRATROPIUM BROMIDE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    irbesartan = models.IntegerField(db_column='IRBESARTAN', blank=True, null=True)  # Field name made lowercase.
    isosorbide_mononitrate_er = models.IntegerField(db_column='ISOSORBIDE MONONITRATE ER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jantoven = models.IntegerField(db_column='JANTOVEN', blank=True, null=True)  # Field name made lowercase.
    janumet = models.IntegerField(db_column='JANUMET', blank=True, null=True)  # Field name made lowercase.
    januvia = models.IntegerField(db_column='JANUVIA', blank=True, null=True)  # Field name made lowercase.
    ketoconazole = models.IntegerField(db_column='KETOCONAZOLE', blank=True, null=True)  # Field name made lowercase.
    klor_con_10 = models.IntegerField(db_column='KLOR CON 10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    klor_con_m10 = models.IntegerField(db_column='KLOR CON M10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    klor_con_m20 = models.IntegerField(db_column='KLOR CON M20', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    labetalol_hcl = models.IntegerField(db_column='LABETALOL HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lactulose = models.IntegerField(db_column='LACTULOSE', blank=True, null=True)  # Field name made lowercase.
    lamotrigine = models.IntegerField(db_column='LAMOTRIGINE', blank=True, null=True)  # Field name made lowercase.
    lansoprazole = models.IntegerField(db_column='LANSOPRAZOLE', blank=True, null=True)  # Field name made lowercase.
    lantus = models.IntegerField(db_column='LANTUS', blank=True, null=True)  # Field name made lowercase.
    lantus_solostar = models.IntegerField(db_column='LANTUS SOLOSTAR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    latanoprost = models.IntegerField(db_column='LATANOPROST', blank=True, null=True)  # Field name made lowercase.
    levemir = models.IntegerField(db_column='LEVEMIR', blank=True, null=True)  # Field name made lowercase.
    levemir_flexpen = models.IntegerField(db_column='LEVEMIR FLEXPEN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    levetiracetam = models.IntegerField(db_column='LEVETIRACETAM', blank=True, null=True)  # Field name made lowercase.
    levofloxacin = models.IntegerField(db_column='LEVOFLOXACIN', blank=True, null=True)  # Field name made lowercase.
    levothyroxine_sodium = models.IntegerField(db_column='LEVOTHYROXINE SODIUM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lidocaine = models.IntegerField(db_column='LIDOCAINE', blank=True, null=True)  # Field name made lowercase.
    lisinopril = models.IntegerField(db_column='LISINOPRIL', blank=True, null=True)  # Field name made lowercase.
    lisinopril_hydrochlorothiazide = models.IntegerField(db_column='LISINOPRIL HYDROCHLOROTHIAZIDE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lithium_carbonate = models.IntegerField(db_column='LITHIUM CARBONATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lorazepam = models.IntegerField(db_column='LORAZEPAM', blank=True, null=True)  # Field name made lowercase.
    losartan_hydrochlorothiazide = models.IntegerField(db_column='LOSARTAN HYDROCHLOROTHIAZIDE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    losartan_potassium = models.IntegerField(db_column='LOSARTAN POTASSIUM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lovastatin = models.IntegerField(db_column='LOVASTATIN', blank=True, null=True)  # Field name made lowercase.
    lovaza = models.IntegerField(db_column='LOVAZA', blank=True, null=True)  # Field name made lowercase.
    lumigan = models.IntegerField(db_column='LUMIGAN', blank=True, null=True)  # Field name made lowercase.
    lyrica = models.IntegerField(db_column='LYRICA', blank=True, null=True)  # Field name made lowercase.
    meclizine_hcl = models.IntegerField(db_column='MECLIZINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meloxicam = models.IntegerField(db_column='MELOXICAM', blank=True, null=True)  # Field name made lowercase.
    metformin_hcl = models.IntegerField(db_column='METFORMIN HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metformin_hcl_er = models.IntegerField(db_column='METFORMIN HCL ER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    methadone_hcl = models.IntegerField(db_column='METHADONE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    methocarbamol = models.IntegerField(db_column='METHOCARBAMOL', blank=True, null=True)  # Field name made lowercase.
    methotrexate = models.IntegerField(db_column='METHOTREXATE', blank=True, null=True)  # Field name made lowercase.
    methylprednisolone = models.IntegerField(db_column='METHYLPREDNISOLONE', blank=True, null=True)  # Field name made lowercase.
    metoclopramide_hcl = models.IntegerField(db_column='METOCLOPRAMIDE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metolazone = models.IntegerField(db_column='METOLAZONE', blank=True, null=True)  # Field name made lowercase.
    metoprolol_succinate = models.IntegerField(db_column='METOPROLOL SUCCINATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metoprolol_tartrate = models.IntegerField(db_column='METOPROLOL TARTRATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metronidazole = models.IntegerField(db_column='METRONIDAZOLE', blank=True, null=True)  # Field name made lowercase.
    mirtazapine = models.IntegerField(db_column='MIRTAZAPINE', blank=True, null=True)  # Field name made lowercase.
    montelukast_sodium = models.IntegerField(db_column='MONTELUKAST SODIUM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    morphine_sulfate = models.IntegerField(db_column='MORPHINE SULFATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    morphine_sulfate_er = models.IntegerField(db_column='MORPHINE SULFATE ER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mupirocin = models.IntegerField(db_column='MUPIROCIN', blank=True, null=True)  # Field name made lowercase.
    nabumetone = models.IntegerField(db_column='NABUMETONE', blank=True, null=True)  # Field name made lowercase.
    namenda = models.IntegerField(db_column='NAMENDA', blank=True, null=True)  # Field name made lowercase.
    namenda_xr = models.IntegerField(db_column='NAMENDA XR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    naproxen = models.IntegerField(db_column='NAPROXEN', blank=True, null=True)  # Field name made lowercase.
    nasonex = models.IntegerField(db_column='NASONEX', blank=True, null=True)  # Field name made lowercase.
    nexium = models.IntegerField(db_column='NEXIUM', blank=True, null=True)  # Field name made lowercase.
    niacin_er = models.IntegerField(db_column='NIACIN ER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nifedical_xl = models.IntegerField(db_column='NIFEDICAL XL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nifedipine_er = models.IntegerField(db_column='NIFEDIPINE ER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nitrofurantoin_mono_macro = models.IntegerField(db_column='NITROFURANTOIN MONO MACRO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nitrostat = models.IntegerField(db_column='NITROSTAT', blank=True, null=True)  # Field name made lowercase.
    nortriptyline_hcl = models.IntegerField(db_column='NORTRIPTYLINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    novolog = models.IntegerField(db_column='NOVOLOG', blank=True, null=True)  # Field name made lowercase.
    novolog_flexpen = models.IntegerField(db_column='NOVOLOG FLEXPEN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nystatin = models.IntegerField(db_column='NYSTATIN', blank=True, null=True)  # Field name made lowercase.
    olanzapine = models.IntegerField(db_column='OLANZAPINE', blank=True, null=True)  # Field name made lowercase.
    omeprazole = models.IntegerField(db_column='OMEPRAZOLE', blank=True, null=True)  # Field name made lowercase.
    ondansetron_hcl = models.IntegerField(db_column='ONDANSETRON HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ondansetron_odt = models.IntegerField(db_column='ONDANSETRON ODT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    onglyza = models.IntegerField(db_column='ONGLYZA', blank=True, null=True)  # Field name made lowercase.
    oxcarbazepine = models.IntegerField(db_column='OXCARBAZEPINE', blank=True, null=True)  # Field name made lowercase.
    oxybutynin_chloride = models.IntegerField(db_column='OXYBUTYNIN CHLORIDE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    oxybutynin_chloride_er = models.IntegerField(db_column='OXYBUTYNIN CHLORIDE ER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    oxycodone_acetaminophen = models.IntegerField(db_column='OXYCODONE ACETAMINOPHEN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    oxycodone_hcl = models.IntegerField(db_column='OXYCODONE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    oxycontin = models.IntegerField(db_column='OXYCONTIN', blank=True, null=True)  # Field name made lowercase.
    pantoprazole_sodium = models.IntegerField(db_column='PANTOPRAZOLE SODIUM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    paroxetine_hcl = models.IntegerField(db_column='PAROXETINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phenobarbital = models.IntegerField(db_column='PHENOBARBITAL', blank=True, null=True)  # Field name made lowercase.
    phenytoin_sodium_extended = models.IntegerField(db_column='PHENYTOIN SODIUM EXTENDED', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pioglitazone_hcl = models.IntegerField(db_column='PIOGLITAZONE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    polyethylene_glycol_3350 = models.IntegerField(db_column='POLYETHYLENE GLYCOL 3350', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    potassium_chloride = models.IntegerField(db_column='POTASSIUM CHLORIDE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pradaxa = models.IntegerField(db_column='PRADAXA', blank=True, null=True)  # Field name made lowercase.
    pramipexole_dihydrochloride = models.IntegerField(db_column='PRAMIPEXOLE DIHYDROCHLORIDE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pravastatin_sodium = models.IntegerField(db_column='PRAVASTATIN SODIUM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prednisone = models.IntegerField(db_column='PREDNISONE', blank=True, null=True)  # Field name made lowercase.
    premarin = models.IntegerField(db_column='PREMARIN', blank=True, null=True)  # Field name made lowercase.
    primidone = models.IntegerField(db_column='PRIMIDONE', blank=True, null=True)  # Field name made lowercase.
    proair_hfa = models.IntegerField(db_column='PROAIR HFA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    promethazine_hcl = models.IntegerField(db_column='PROMETHAZINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    propranolol_hcl = models.IntegerField(db_column='PROPRANOLOL HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    propranolol_hcl_er = models.IntegerField(db_column='PROPRANOLOL HCL ER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quetiapine_fumarate = models.IntegerField(db_column='QUETIAPINE FUMARATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quinapril_hcl = models.IntegerField(db_column='QUINAPRIL HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    raloxifene_hcl = models.IntegerField(db_column='RALOXIFENE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ramipril = models.IntegerField(db_column='RAMIPRIL', blank=True, null=True)  # Field name made lowercase.
    ranexa = models.IntegerField(db_column='RANEXA', blank=True, null=True)  # Field name made lowercase.
    ranitidine_hcl = models.IntegerField(db_column='RANITIDINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    restasis = models.IntegerField(db_column='RESTASIS', blank=True, null=True)  # Field name made lowercase.
    risperidone = models.IntegerField(db_column='RISPERIDONE', blank=True, null=True)  # Field name made lowercase.
    ropinirole_hcl = models.IntegerField(db_column='ROPINIROLE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    seroquel_xr = models.IntegerField(db_column='SEROQUEL XR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sertraline_hcl = models.IntegerField(db_column='SERTRALINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    simvastatin = models.IntegerField(db_column='SIMVASTATIN', blank=True, null=True)  # Field name made lowercase.
    sotalol = models.IntegerField(db_column='SOTALOL', blank=True, null=True)  # Field name made lowercase.
    spiriva = models.IntegerField(db_column='SPIRIVA', blank=True, null=True)  # Field name made lowercase.
    spironolactone = models.IntegerField(db_column='SPIRONOLACTONE', blank=True, null=True)  # Field name made lowercase.
    sucralfate = models.IntegerField(db_column='SUCRALFATE', blank=True, null=True)  # Field name made lowercase.
    sulfamethoxazole_trimethoprim = models.IntegerField(db_column='SULFAMETHOXAZOLE TRIMETHOPRIM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sumatriptan_succinate = models.IntegerField(db_column='SUMATRIPTAN SUCCINATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    symbicort = models.IntegerField(db_column='SYMBICORT', blank=True, null=True)  # Field name made lowercase.
    synthroid = models.IntegerField(db_column='SYNTHROID', blank=True, null=True)  # Field name made lowercase.
    tamsulosin_hcl = models.IntegerField(db_column='TAMSULOSIN HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    temazepam = models.IntegerField(db_column='TEMAZEPAM', blank=True, null=True)  # Field name made lowercase.
    terazosin_hcl = models.IntegerField(db_column='TERAZOSIN HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    timolol_maleate = models.IntegerField(db_column='TIMOLOL MALEATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tizanidine_hcl = models.IntegerField(db_column='TIZANIDINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tolterodine_tartrate_er = models.IntegerField(db_column='TOLTERODINE TARTRATE ER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    topiramate = models.IntegerField(db_column='TOPIRAMATE', blank=True, null=True)  # Field name made lowercase.
    toprol_xl = models.IntegerField(db_column='TOPROL XL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    torsemide = models.IntegerField(db_column='TORSEMIDE', blank=True, null=True)  # Field name made lowercase.
    tramadol_hcl = models.IntegerField(db_column='TRAMADOL HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    travatan_z = models.IntegerField(db_column='TRAVATAN Z', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trazodone_hcl = models.IntegerField(db_column='TRAZODONE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    triamcinolone_acetonide = models.IntegerField(db_column='TRIAMCINOLONE ACETONIDE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    triamterene_hydrochlorothiazid = models.IntegerField(db_column='TRIAMTERENE HYDROCHLOROTHIAZID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    valacyclovir = models.IntegerField(db_column='VALACYCLOVIR', blank=True, null=True)  # Field name made lowercase.
    valsartan = models.IntegerField(db_column='VALSARTAN', blank=True, null=True)  # Field name made lowercase.
    valsartan_hydrochlorothiazide = models.IntegerField(db_column='VALSARTAN HYDROCHLOROTHIAZIDE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    venlafaxine_hcl = models.IntegerField(db_column='VENLAFAXINE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    venlafaxine_hcl_er = models.IntegerField(db_column='VENLAFAXINE HCL ER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ventolin_hfa = models.IntegerField(db_column='VENTOLIN HFA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    verapamil_er = models.IntegerField(db_column='VERAPAMIL ER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vesicare = models.IntegerField(db_column='VESICARE', blank=True, null=True)  # Field name made lowercase.
    voltaren = models.IntegerField(db_column='VOLTAREN', blank=True, null=True)  # Field name made lowercase.
    vytorin = models.IntegerField(db_column='VYTORIN', blank=True, null=True)  # Field name made lowercase.
    warfarin_sodium = models.IntegerField(db_column='WARFARIN SODIUM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xarelto = models.IntegerField(db_column='XARELTO', blank=True, null=True)  # Field name made lowercase.
    zetia = models.IntegerField(db_column='ZETIA', blank=True, null=True)  # Field name made lowercase.
    ziprasidone_hcl = models.IntegerField(db_column='ZIPRASIDONE HCL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    zolpidem_tartrate = models.IntegerField(db_column='ZOLPIDEM TARTRATE', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return self.fname + ' ' + self.lname
    class Meta:
        managed = False
        db_table = 'Prescriber'
        indexes = [
            models.Index(fields=['lname', 'fname']),
            models.Index(fields=['fname'], name='fname_idx'),
        ]


class Statedata(models.Model):
    state = models.CharField(db_column='State', max_length=50)  # Field name made lowercase.
    stateabbrev = models.CharField(db_column='StateAbbrev', primary_key=True, max_length=2)  # Field name made lowercase.
    population = models.BigIntegerField(db_column='Population', blank=True, null=True)  # Field name made lowercase.
    deaths = models.IntegerField(db_column='Deaths', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.state
    class Meta:
        managed = False
        db_table = 'StateData'


class Triple(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    prescriberid = models.ForeignKey(Prescriber, models.DO_NOTHING, db_column='PrescriberID')  # Field name made lowercase.
    drugname = models.ForeignKey(Drugs, models.DO_NOTHING, db_column='DrugName')  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Triple'

class TopTenWorst(models.Model):
    prescriberid = models.BigIntegerField(blank=True, null=True)
    fname = models.CharField(db_column='Fname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    credentials = models.CharField(max_length=50, blank=True, null=True)
    specialty = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'top_ten_worst'


class PrescriberPercentile(models.Model):
    prescriberid = models.BigIntegerField(db_column='PrescriberID', primary_key=True)  # Field name made lowercase.
    percentile = models.FloatField()

    class Meta:
        managed = False
        db_table = 'prescriber_percentile'

class Averages(models.Model):
    drugname = models.CharField(max_length=50, blank=True, null=True)
    avg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'averages'