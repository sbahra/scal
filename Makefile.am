# We'll add the programs throughout the Makefile.
bin_PROGRAMS =
noinst_PROGRAMS =
TESTS =

AM_CPPFLAGS = -Werror -mcx16 -m64  -std=c++0x \
        @CC_OPTIMIZATION@ \
        -I${top_srcdir}/src \
        -ffast-math \
        -fno-builtin-malloc \
        -fno-builtin-calloc \
        -fno-builtin-realloc \
        -fno-builtin-free \
        -fno-omit-frame-pointer \
	@GFLAGS_CFLAGS@

AM_LDFLAGS = -Wl,--as-needed
LDADD = @GFLAGS_LIBS@

DATASTRUCTURE_INCLUDES = \
	src/datastructures/balancer_1random.h \
	src/datastructures/balancer.h \
	src/datastructures/balancer_id.h \
	src/datastructures/balancer_partrr.h \
	src/datastructures/boundedsize_kfifo.h \
	src/datastructures/distributed_queue.h \
	src/datastructures/distributed_queue_interface.h \
	src/datastructures/flatcombining_queue.h \
	src/datastructures/kstack.h \
	src/datastructures/lockbased_queue.h \
	src/datastructures/ms_queue.h \
	src/datastructures/pool.h \
	src/datastructures/queue.h \
	src/datastructures/random_dequeue_queue.h \
	src/datastructures/single_list.h \
	src/datastructures/stack.h \
	src/datastructures/treiber_stack.h \
	src/datastructures/unboundedsize_kfifo.h \
	src/datastructures/wf_queue_ppopp11.h \
	src/datastructures/wf_queue_ppopp12.h \
	src/datastructures/ts_stack.h \
	src/datastructures/ts_queue.h \
	src/datastructures/ts_deque.h \
	src/datastructures/ts_timestamp.h \
	src/datastructures/ts_stack_buffer.h \
	src/datastructures/ts_queue_buffer.h \
	src/datastructures/ts_deque_buffer.h \
	src/datastructures/dts_queue.h

noinst_HEADERS = \
	$(DATASTRUCTURE_INCLUDES) \
	src/benchmark/common.h \
	src/benchmark/std_glue/std_pipe_api.h \
	src/util/atomic_value.h \
	src/util/atomic_value128.h \
	src/util/atomic_value64_base.h \
	src/util/atomic_value64_offset.h \
	src/util/atomic_value64_no_offset.h

UTIL_OBJS = \
	src/util/atomic_value128.h \
	src/util/atomic_value128_unittest-malloc.o \
	src/util/atomic_value64_base.h \
	src/util/atomic_value64_no_offset.h \
	src/util/atomic_value64_offset.h \
	src/util/atomic_value.h \
	src/util/barrier.h \
	src/util/bitmap.h \
	src/util/malloc.h \
        src/util/malloc.cc \
        src/util/operation_logger.h \
        src/util/platform.h \
        src/util/random.h \
        src/util/random.cc \
        src/util/threadlocals.h \
        src/util/threadlocals.cc \
	src/util/time.h \
	src/util/workloads.h \
	src/util/workloads.cc

#
# BFS graph benchmark
#

bin_PROGRAMS += bfs-analyzer
bfs_analyzer_SOURCES = \
	$(UTIL_OBJS) \
        src/benchmark/bfs/bfs_analyzer.cc \
	src/benchmark/bfs/graph.h \
        src/benchmark/bfs/graph.cc

bin_PROGRAMS += bfs-sequential
bfs_sequential_SOURCES = \
	$(UTIL_OBJS) \
        src/benchmark/bfs/bfs_sequential.cc \
	src/benchmark/bfs/graph.h \
        src/benchmark/bfs/graph.cc

#
# Producer/Consumer benchmark
#

PRODCON_BASE_OBJS = \
	$(UTIL_OBJS) \
        src/benchmark/common.cc \
        src/benchmark/prodcon/prodcon.cc

bin_PROGRAMS += prodcon-bskfifo
prodcon_bskfifo_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_bskfifo.cc

bin_PROGRAMS += prodcon-fc
prodcon_fc_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_fc_queue.cc

bin_PROGRAMS += prodcon-lb
prodcon_lb_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_lb_queue.cc

bin_PROGRAMS += prodcon-kstack
prodcon_kstack_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_kstack.cc

bin_PROGRAMS += prodcon-ms
prodcon_ms_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_ms_queue.cc

bin_PROGRAMS += prodcon-dq-1random
prodcon_dq_1random_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_dq_1random.cc

bin_PROGRAMS += prodcon-dq-1random-tstack
prodcon_dq_1random_tstack_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_dq_1random_tstack.cc

bin_PROGRAMS += prodcon-dq-partrr
prodcon_dq_partrr_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_dq_partrr.cc

bin_PROGRAMS += prodcon-rd
prodcon_rd_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_rd_queue.cc

bin_PROGRAMS += prodcon-tstack
prodcon_tstack_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_treiber_stack.cc

bin_PROGRAMS += prodcon-uskfifo
prodcon_uskfifo_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_uskfifo.cc

bin_PROGRAMS += prodcon-wf-ppopp11
prodcon_wf_ppopp11_SOURCES = \
	$(PRODCON_BASE_OBJS) \
	src/benchmark/std_glue/glue_wf_ppopp11.cc

bin_PROGRAMS += prodcon-wf-ppopp12
prodcon_wf_ppopp12_SOURCES = \
	$(PRODCON_BASE_OBJS) \
	src/benchmark/std_glue/glue_wf_ppopp12.cc

bin_PROGRAMS += prodcon-hc-ts-interval-stack
prodcon_hc_ts_interval_stack_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_hardcoded_ts_interval_stack.cc

bin_PROGRAMS += prodcon-hc-ts-atomic-stack
prodcon_hc_ts_atomic_stack_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_hardcoded_ts_atomic_stack.cc

bin_PROGRAMS += prodcon-hc-ts-stutter-stack
prodcon_hc_ts_stutter_stack_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_hardcoded_ts_stutter_stack.cc

bin_PROGRAMS += prodcon-hc-ts-interval-queue
prodcon_hc_ts_interval_queue_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_hardcoded_ts_interval_queue.cc

bin_PROGRAMS += prodcon-hc-ts-hardware-stack
prodcon_hc_ts_hardware_stack_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_hardcoded_ts_hardware_stack.cc

bin_PROGRAMS += prodcon-hc-ts-hardware-queue
prodcon_hc_ts_hardware_queue_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_hardcoded_ts_hardware_queue.cc

bin_PROGRAMS += prodcon-ts-interval-stack
prodcon_ts_interval_stack_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_ts_interval_stack.cc

bin_PROGRAMS += prodcon-ts-interval-queue
prodcon_ts_interval_queue_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_ts_interval_queue.cc

bin_PROGRAMS += prodcon-ts-hardware-stack
prodcon_ts_hardware_stack_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_ts_hardware_stack.cc

bin_PROGRAMS += prodcon-ts-hardware-queue
prodcon_ts_hardware_queue_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_ts_hardware_queue.cc

bin_PROGRAMS += prodcon-ts-interval-deque
prodcon_ts_interval_deque_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_ts_interval_deque.cc

bin_PROGRAMS += prodcon-ts-hardware-deque
prodcon_ts_hardware_deque_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_ts_hardware_deque.cc

bin_PROGRAMS += prodcon-ts-atomic-queue
prodcon_ts_atomic_queue_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_ts_atomic_queue.cc

bin_PROGRAMS += prodcon-ts-stutter-queue
prodcon_ts_stutter_queue_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_ts_stutter_queue.cc

bin_PROGRAMS += prodcon-dts-queue
prodcon_dts_queue_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_dts_queue.cc

bin_PROGRAMS += prodcon-eb-stack
prodcon_eb_stack_SOURCES = \
        $(PRODCON_BASE_OBJS) \
        src/benchmark/std_glue/glue_eb_stack.cc

#
# SPF benchmark
#

bin_PROGRAMS += spf-sequential
spf_sequential_SOURCES = \
	$(UTIL_OBJS) \
        src/benchmark/bfs/spf_sequential.cc \
	src/benchmark/bfs/graph.h \
        src/benchmark/bfs/graph.cc

#
# Tests -- currenctly only the atomic containers
#

gtest:
	$(AM_V_GEN)mkdir -p gtest
	cd gtest ; cmake /usr/src/gtest
	$(AM_V_GEN)make -C gtest all

gtest/libgtest_main.a: gtest

gtest/libgtest.a: gtest

gtest-clean:
	$(AM_V_GEN)rm -rf gtest

GTEST_LIBS = gtest/libgtest.a gtest/libgtest_main.a

TEST_CPPFLAGS = -Werror -mcx16 -m64 -std=c++0x \
	@CC_OPTIMIZATION@ \
        -I${top_srcdir}/src \
        -ffast-math \
        -fno-builtin-malloc \
        -fno-builtin-calloc \
        -fno-builtin-realloc \
        -fno-builtin-free \
        -fno-omit-frame-pointer \
	@GFLAGS_CFLAGS@

TESTS += atomic_value128_unittest
atomic_value128_unittest_CPPFLAGS = \
	$(TEST_CPPFLAGS)
atomic_value128_unittest_LDADD = \
        @GFLAGS_LIBS@ \
        $(GTEST_LIBS)
atomic_value128_unittest_SOURCES = \
        src/test/atomic_value128_unittest.cc \
        src/util/malloc.cc

TESTS += atomic_value64_no_offset_unittest
atomic_value64_no_offset_unittest_CPPFLAGS = \
	$(TEST_CPPFLAGS)
atomic_value64_no_offset_unittest_LDADD = \
        @GFLAGS_LIBS@ \
        $(GTEST_LIBS)
atomic_value64_no_offset_unittest_SOURCES = \
        src/test/atomic_value64_no_offset_unittest.cc \
        src/util/malloc.cc

TESTS += atomic_value64_offset_unittest
atomic_value64_offset_unittest_CPPFLAGS = \
	$(TEST_CPPFLAGS)
atomic_value64_offset_unittest_LDADD = \
        @GFLAGS_LIBS@ \
        $(GTEST_LIBS)
atomic_value64_offset_unittest_SOURCES = \
        src/test/atomic_value64_offset_unittest.cc \
        src/util/malloc.cc

TESTS += random_unittest
random_unittest_CPPFLAGS = \
	$(TEST_CPPFLAGS)
random_unittest_LDADD = \
        @GFLAGS_LIBS@ \
        $(GTEST_LIBS)
random_unittest_SOURCES = \
        src/test/random_unittest.cc \
        src/util/random.cc \
        src/util/threadlocals.cc

noinst_PROGRAMS += $(TESTS)

#
# Extend the standard Makefile rules
#

clean-local: gtest-clean

