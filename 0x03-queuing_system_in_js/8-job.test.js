import { expect } from "chai";
import kue from "kue";
import createPushNotificationsJobs from "./8-job";

const queue = kue.createQueue();

describe("createPushNotificationsJobs", () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array',  () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw(Error, "Jobs is not an array");
  });

  it.skip("create two new jobs to the queue", () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Message 1' },
      { phoneNumber: '0987654321', message: 'Message 2' }
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});
