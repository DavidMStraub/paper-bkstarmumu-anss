from flavio.statistics.fits import FastFit

# list of observables included in the fit
# careful! Including S_i and P'_i observables is only consistent this way
# (no double-counting) because ATLAS and LHCb use different bins.

observables = [
 ('<FL>(B0->K*mumu)', 0.04, 2),
 ('<FL>(B0->K*mumu)', 2, 4),
 ('<FL>(B0->K*mumu)', 4, 6),
 ('<FL>(B0->K*mumu)', 0, 2),
 ('<FL>(B0->K*mumu)', 1, 2),
 ('<FL>(B0->K*mumu)', 2, 4.3),
 ('<FL>(B0->K*mumu)', 4.3, 6),
 ('<FL>(B0->K*mumu)', 1.1, 2.5),
 ('<FL>(B0->K*mumu)', 2.5, 4),
 ('<FL>(B0->K*mumu)', 15, 19),
 ('<FL>(Bs->phimumu)', 2.0, 5.0),
 ('<FL>(Bs->phimumu)', 15.0, 19.0),

 ('<P1>(B0->K*mumu)', 0.04, 2),
 ('<P1>(B0->K*mumu)', 2, 4),
 ('<P1>(B0->K*mumu)', 4, 6),
 ('<P1>(B0->K*mumu)', 1, 2),
 ('<P1>(B0->K*mumu)', 2, 4.3),
 ('<P1>(B0->K*mumu)', 4.3, 6),

 ('<P4p>(B0->K*mumu)', 0.04, 2),
 ('<P4p>(B0->K*mumu)', 2, 4),
 ('<P4p>(B0->K*mumu)', 4, 6),

 ('<P5p>(B0->K*mumu)', 0.04, 2),
 ('<P5p>(B0->K*mumu)', 2, 4),
 ('<P5p>(B0->K*mumu)', 4, 6),
 ('<P5p>(B0->K*mumu)', 1, 2),
 ('<P5p>(B0->K*mumu)', 2, 4.3),
 ('<P5p>(B0->K*mumu)', 4.3, 6),

 ('<AFB>(B0->K*mumu)', 1.1, 2.5),
 ('<AFB>(B0->K*mumu)', 2.5, 4),
 ('<AFB>(B0->K*mumu)', 4.3, 6),
 ('<AFB>(B0->K*mumu)', 4, 6),
 ('<AFB>(B0->K*mumu)', 15, 19),
 ('<AFB>(B0->K*mumu)', 0, 2),
 ('<AFB>(B0->K*mumu)', 2, 4.3),
 ('<AFB>(B0->K*mumu)', 1, 2),

 ('<S3>(B0->K*mumu)', 1.1, 2.5),
 ('<S3>(B0->K*mumu)', 2.5, 4),
 ('<S3>(B0->K*mumu)', 4, 6),
 ('<S3>(B0->K*mumu)', 15, 19),
 ('<S3>(Bs->phimumu)', 2.0, 5.0),
 ('<S3>(Bs->phimumu)', 15.0, 19.0),

 ('<S4>(B0->K*mumu)', 1.1, 2.5),
 ('<S4>(B0->K*mumu)', 2.5, 4),
 ('<S4>(B0->K*mumu)', 4, 6),
 ('<S4>(B0->K*mumu)', 15, 19),
 ('<S4>(Bs->phimumu)', 2.0, 5.0),
 ('<S4>(Bs->phimumu)', 15.0, 19.0),

 ('<S5>(B0->K*mumu)', 1.1, 2.5),
 ('<S5>(B0->K*mumu)', 2.5, 4),
 ('<S5>(B0->K*mumu)', 4, 6),
 ('<S5>(B0->K*mumu)', 15, 19),

 ('<dBR/dq2>(B+->K*mumu)', 2.0, 4.0),
 ('<dBR/dq2>(B+->K*mumu)', 4.0, 6.0),
 ('<dBR/dq2>(B+->K*mumu)', 15.0, 19.0),
 ('<dBR/dq2>(B+->K*mumu)', 0, 2),
 ('<dBR/dq2>(B+->K*mumu)', 2, 4.3),

 ('<dBR/dq2>(B0->K*mumu)', 1, 2),
 ('<dBR/dq2>(B0->K*mumu)', 1.1, 2.5),
 ('<dBR/dq2>(B0->K*mumu)', 2.5, 4.0),
 ('<dBR/dq2>(B0->K*mumu)', 4.0, 6.0),
 ('<dBR/dq2>(B0->K*mumu)', 15.0, 19.0),
 ('<dBR/dq2>(B0->K*mumu)', 0, 2),
 ('<dBR/dq2>(B0->K*mumu)', 2, 4.3),
 ('<dBR/dq2>(B0->K*mumu)', 4.3, 6),

 ('<dBR/dq2>(Bs->phimumu)', 1.0, 6.0),
 ('<dBR/dq2>(Bs->phimumu)', 15.0, 19.0),

 ('<dBR/dq2>(B+->Kmumu)', 1.1, 2.0),
 ('<dBR/dq2>(B+->Kmumu)', 2.0, 3.0),
 ('<dBR/dq2>(B+->Kmumu)', 3.0, 4.0),
 ('<dBR/dq2>(B+->Kmumu)', 4.0, 5.0),
 ('<dBR/dq2>(B+->Kmumu)', 5.0, 6.0),
 ('<dBR/dq2>(B+->Kmumu)', 15.0, 22.0),
 ('<dBR/dq2>(B+->Kmumu)', 0, 2),
 ('<dBR/dq2>(B+->Kmumu)', 2, 4.3),

 ('<dBR/dq2>(B0->Kmumu)', 2.0, 4.0),
 ('<dBR/dq2>(B0->Kmumu)', 4.0, 6.0),
 ('<dBR/dq2>(B0->Kmumu)', 15.0, 22.0),
 ('<dBR/dq2>(B0->Kmumu)', 0, 2),
 ('<dBR/dq2>(B0->Kmumu)', 2, 4.3),

 ('<BR>(B->Xsmumu)', 1.0, 6.0),
 ('<BR>(B->Xsmumu)', 14.2, 25.0),
]

# list of measurements to be included in the fit
measurements = [
 'ATLAS B->K*mumu 2017 FL',
 'ATLAS B->K*mumu 2017 P1',
 'ATLAS B->K*mumu 2017 P4p',
 'ATLAS B->K*mumu 2017 P5p',

 'CMS B->K*mumu 2013 combined with 2015',
 'CMS B->K*mumu 2015 4.3-6',
 'CMS B->K*mumu 2017 P1',
 'CMS B->K*mumu 2017 P5p',

 'LHCb B->K*mumu 2015 S 1.1-2.5',
 'LHCb B->K*mumu 2015 S 15-19',
 'LHCb B->K*mumu 2015 S 2.5-4',
 'LHCb B->K*mumu 2015 S 4-6',
 'LHCb Bs->phimumu 2015 15.0-19.0 GeV^2',
 'LHCb Bs->phimumu 2015 1.0-6.0 GeV^2',
 'LHCb Bs->phimumu 2015 2.0-5.0 GeV^2',

 'LHCb B+->K*mumu BR 2014',
 'LHCb B0->K*mumu BR 2016',
 'LHCb B+->Kmumu BR 2014',
 'LHCb B0->Kmumu BR 2014',
 'LHCb Bs->phimumu BR 2015',
 'BaBar B->Xll 2013',
 'CDF Bs->phimumu 2012',
 'CDF B0->Kmumu 2012',
 'CDF B+>Kmumu 2012',
 'CDF B0->K*mumu BR 2012',
 'CDF B+->K*mumu 2012',

'CDF B0->K*mumu FL 2012',
'CDF B0->K*mumu AFB 2012',
]

# Wilson coefficient function
def wc_fct(ReC9, ReC10):
    return {
    'C9_bsmumu':  ReC9,
    'C10_bsmumu':  ReC10,
    }

# FastFit instance
fit = FastFit("Global semi-leptonic b->s fit",
            nuisance_parameters = 'all',
            observables = observables,
            fit_wc_function = wc_fct,
            include_measurements = measurements,
            input_scale = 4.8,
        )
