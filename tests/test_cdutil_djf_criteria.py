import cdms2
import numpy
import unittest
import cdutil
import MV2

class CDUTIL(unittest.TestCase):
    def testDJFCriteria(self):
        data = [1,]*12+[2,]*12

        print(data)

        months = list(range(24))

        t=cdms2.createAxis(months)
        t.designateTime()
        t.units="months since 2014"


        cdutil.setTimeBoundsMonthly(t)
        data = numpy.array(data)
        data=MV2.array(data)
        data.setAxis(0,t)
        print(t.asComponentTime())
        djf = cdutil.times.DJF(data)
        djfc = cdutil.times.DJF.climatology(data)
        print(djf)
        self.assertTrue(numpy.allclose(djf[0],1.) and numpy.allclose(djf[1],1.6666667) and numpy.allclose(djf[2],2.))
        print(djfc)
        self.assertTrue(numpy.allclose(djfc,1.625))
        djf = cdutil.times.DJF(data,criteriaarg=[.5,None])
        djfc = cdutil.times.DJF.climatology(data,criteriaarg=[.5,None])

        print(djf)
        self.assertTrue(numpy.ma.allclose(djf[0],1.) and numpy.ma.allclose(djf[1],1.6666667) and numpy.ma.allclose(djf[2],numpy.ma.masked))
        print(djfc)
        self.assertTrue(numpy.allclose(djfc,1.4))
